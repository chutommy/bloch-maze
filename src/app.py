import sys

import pygame

from config import *
from game import GameState, Game
from level import get_levels
from render import Render


class App:
    """Handles the whole runtime of the game."""

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
        self.render.render_welcome()
        self.wait_response()

    def display_end(self):
        self.render.render_end()
        self.wait_response(ENDING_DELAY)

    def display_current_level_header(self):
        self.render.render_banner(f"level {self.current_level_number}", self.levels[self.current_level_number].title)
        self.wait_response()

    def display_current_level_end(self):
        self.render.render_banner(f"successfully finished level {self.current_level_number}", WELL_DONE_TXT)
        self.wait_response()

    def level_up(self):
        self.current_level_number += 1
        if self.current_level_number >= len(self.levels):
            self.current_level_number = len(self.levels) - 1
            return False
        return True

    def level_down(self):
        self.current_level_number -= 1
        if self.current_level_number <= 0:
            self.current_level_number = 0
            return False
        return True

    def run_level(self):
        game = Game(self.levels[self.current_level_number])
        self.display_current_level_header()
        prev_rect = self.render.draw_game(game, game.level.start_state)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()

            match game.state:
                case GameState.JUMP:
                    return True
                case GameState.SUCCESS:
                    self.display_current_level_end()
                    return self.level_up()
                case GameState.FAIL:
                    game.__init__(game.level)
                    prev_rect = self.render.draw_game(game, game.level.start_state)
                    pygame.time.wait(FAIL_DELAY)

            prev_player = game.player
            if self.handle_keys(game, pygame.key.get_pressed()):
                prev_rect = self.update_player(game, prev_player, prev_rect)

            self.clock.tick(FPS)

    def update_player(self, game, prev_player, prev_rect):
        self.render.draw_cell(game.maze, prev_player.x, prev_player.y, game.level.start_state, game.level.end_state)
        new_rect = self.render.draw_player(game.maze, game.player, game.player_state)
        pygame.display.update(prev_rect)
        pygame.display.update(new_rect)
        return new_rect

    def run(self):
        while True:
            self.display_welcome()
            while self.run_level():
                pass
            self.display_end()
            self.current_level_number = 1

    def handle_keys(self, game, keys):
        if keys[pygame.K_r]:
            game.set_fail()
            return False
        if keys[pygame.K_p]:
            game.set_jump()
            self.level_down()
            return False
        if keys[pygame.K_n]:
            game.set_jump()
            self.level_up()
            return False

        if keys[pygame.K_UP] + keys[pygame.K_DOWN] + keys[pygame.K_RIGHT] + keys[pygame.K_LEFT] \
                + keys[pygame.K_w] + keys[pygame.K_s] + keys[pygame.K_d] + keys[pygame.K_a] == 1:
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                game.move_up()
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                game.move_down()
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                game.move_right()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                game.move_left()
            pygame.time.wait(MOVE_DELAY)
            return True

        return False

    @staticmethod
    def exit():
        pygame.quit()
        sys.exit()

    def wait_response(self, duration=BANNER_DELAY):
        pygame.time.wait(duration)
        pygame.event.clear()
        self.wait_keypress()

    def wait_keypress(self):
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                self.exit()
            elif event.type == pygame.KEYDOWN:
                break
