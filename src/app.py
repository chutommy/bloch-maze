import sys

import pygame

from config import Config
from game import GameState, Game
from level import get_levels
from render import Render


class App:
    """Handles the whole runtime of the game."""

    def __init__(self, config):
        self.cfg = Config(config)

        pygame.init()
        pygame.display.set_caption(self.cfg['caption'])

        icon = pygame.image.load(self.cfg['icons'])
        pygame.display.set_icon(icon)

        self.clock = pygame.time.Clock()
        self.levels = get_levels(self.cfg['levels'], self.cfg['dimensions'])
        self.current_level_number = 1

        fonts = self.cfg['fonts']
        font = pygame.font.Font(fonts['regular'], fonts['regular_size'])
        bfont = pygame.font.Font(fonts['bold'], fonts['bold_size'])

        cell_size = self.cfg['cell_size']
        width = self.cfg['dimensions', 'width'] * cell_size
        height = self.cfg['dimensions', 'height'] * cell_size
        screen = pygame.display.set_mode((width, height))
        self.render = Render(screen, cell_size, font, bfont)

    def run(self):
        while True:
            self.display_welcome()
            while self.run_level():
                pass
            self.display_end()
            self.current_level_number = 1

    def run_level(self):
        game = Game(self.levels[self.current_level_number])
        key = self.display_current_level_header()
        self.handle_nav_key(game, key)
        if game.state == GameState.JUMP:
            return True

        prev_rect = self.render.draw_game(game, game.level.start_state)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()

            prev_player = game.player
            if self.handle_keys(game, pygame.key.get_pressed()):
                prev_rect = self.update_player(game, prev_player, prev_rect)

            match game.state:
                case GameState.JUMP:
                    return True
                case GameState.SUCCESS:
                    if self.cfg['show_level_ending']:
                        self.display_current_level_end()
                    return self.level_up()
                case GameState.FAIL:
                    game.__init__(game.level)
                    prev_rect = self.render.draw_game(game, game.level.start_state)
                    pygame.time.wait(self.cfg['delays', 'fail'])

            self.clock.tick(self.cfg['fps'])

    def display_welcome(self):
        self.render.render_welcome(self.cfg['texts'])
        self.wait_response(self.cfg['delays', 'banner'])

    def display_end(self):
        self.render.render_end(self.cfg['texts'])
        self.wait_response(self.cfg['delays', 'ending'])

    def display_current_level_header(self):
        self.render.render_banner(f'level {self.current_level_number}',
                                  self.levels[self.current_level_number].title,
                                  self.cfg['texts'])
        return self.wait_response(self.cfg['delays', 'banner'])

    def display_current_level_end(self):
        self.render.render_banner(f'successfully finished level {self.current_level_number}',
                                  self.cfg['texts', 'well_done'], self.cfg['texts'])
        return self.wait_response(self.cfg['delays', 'banner'])

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

    def update_player(self, game, prev_player, prev_rect):
        self.render.draw_cell(game.maze, prev_player.x, prev_player.y, game.level.start_state, game.level.end_state)
        new_rect = self.render.draw_player(game.maze, game.player, game.player_state)
        pygame.display.update(prev_rect)
        pygame.display.update(new_rect)
        return new_rect

    def handle_nav_key(self, game, key):
        match key:
            case pygame.K_p:
                game.set_jump()
                self.level_down()
            case pygame.K_n:
                game.set_jump()
                self.level_up()

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
            pygame.time.wait(self.cfg['delays', 'move'])
            return True

        return False

    def wait_response(self, duration):
        pygame.time.wait(duration)
        pygame.event.clear()
        return self.wait_keypress()

    def wait_keypress(self):
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                self.exit()
            elif event.type == pygame.KEYDOWN:
                return event.key

    @staticmethod
    def exit():
        pygame.quit()
        sys.exit()
