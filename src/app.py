import sys

import pygame

from config import *
from game import GameState, Game
from level import get_levels
from render import Render


class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(HEAD)

        icon = pygame.image.load(ICON)
        pygame.display.set_icon(icon)

        self.clock = pygame.time.Clock()
        self.levels, dimensions = get_levels()
        self.current_level_number = 1

        font = pygame.font.Font(FONT, FONT_SIZE)
        bfont = pygame.font.Font(BOLD_FONT, BOLD_FONT_SIZE)

        width = dimensions[1] * CELL_SIZE
        height = dimensions[0] * CELL_SIZE
        screen = pygame.display.set_mode((width, height))
        self.render = Render(screen, CELL_SIZE, font, bfont)

    def display_welcome(self):
        self.render.welcome()
        pygame.display.update()
        pygame.time.wait(BANNER_DELAY)
        pygame.event.clear()
        self.wait_keypress()

    def display_level_header(self):
        lvl = self.levels[self.current_level_number]
        self.render.banner(lvl.title, lvl.subtitle)
        pygame.display.update()
        pygame.time.wait(BANNER_DELAY)
        pygame.event.clear()
        self.wait_keypress()

    def display_level_end(self):
        lvl = self.levels[self.current_level_number]
        self.render.banner(f"successfully finished {lvl.title}", 'well done!')
        pygame.display.update()
        pygame.time.wait(BANNER_DELAY)
        pygame.event.clear()
        self.wait_keypress()

    def level_up(self):
        self.current_level_number += 1
        if self.current_level_number >= len(self.levels):
            self.current_level_number = len(self.levels) - 1

    def level_down(self):
        self.current_level_number -= 1
        if self.current_level_number <= 0:
            self.current_level_number = 0

    def run_level(self):
        lvl = self.levels[self.current_level_number]
        game = Game(lvl)

        self.display_level_header()
        prev_rect = self.render.game(game, game.level.start_state, game.level.end_state, game.level.start_state)
        pygame.display.update()

        running = True
        while running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()

            if game.state == GameState.JUMP:
                return

            if game.state == GameState.SUCCESS:
                self.display_level_end()
                self.level_up()
                return

            if game.state == GameState.FAIL:
                game.__init__(game.level)
                prev_rect = self.render.game(game, game.level.start_state, game.level.end_state, game.level.start_state)
                pygame.display.update()
                pygame.time.wait(FAIL_DELAY)

            prev_player = game.player
            key = pygame.key.get_pressed()
            if self.handle_key(game, key):
                prev_rect = self.update_player(game, prev_player, prev_rect)

    def update_player(self, game, prev_player, prev_rect):
        self.render.cell(game.maze, prev_player.x, prev_player.y, game.level.start_state, game.level.end_state)
        new_rect = self.render.player(game.maze, game.player, game.player_state)

        pygame.display.update(prev_rect)
        pygame.display.update(new_rect)

        return new_rect

    def run(self):
        while True:
            self.run_level()

    @staticmethod
    def exit():
        pygame.quit()
        sys.exit()

    def wait_keypress(self):
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                self.exit()
            elif event.type == pygame.KEYDOWN:
                break

    def handle_key(self, game, key):
        if key[pygame.K_r]:
            game.set_fail()
            return False
        if key[pygame.K_p]:
            game.set_jump()
            self.level_down()
            return False
        if key[pygame.K_n]:
            game.set_jump()
            self.level_up()
            return False

        if key[pygame.K_UP] + key[pygame.K_DOWN] + key[pygame.K_RIGHT] + key[pygame.K_LEFT] \
                + key[pygame.K_w] + key[pygame.K_s] + key[pygame.K_d] + key[pygame.K_a] == 1:
            if key[pygame.K_UP] or key[pygame.K_w]:
                game.move_up()
            if key[pygame.K_DOWN] or key[pygame.K_s]:
                game.move_down()
            if key[pygame.K_RIGHT] or key[pygame.K_d]:
                game.move_right()
            if key[pygame.K_LEFT] or key[pygame.K_a]:
                game.move_left()
            pygame.time.wait(MOVE_DELAY)
            return True

        return False
