import pygame

from cell import CELL_COLORS
from config import *
from maze import Cell

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Render:
    """Manages game rendering."""

    def __init__(self, screen, cell_size, font, bfont):
        self.screen = screen
        self.cell_size = cell_size
        self.font = font
        self.bfont = bfont

    def draw_text(self, text, color, center, bold=False):
        font = self.font if not bold else self.bfont
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=center)
        self.screen.blit(text_surface, text_rect)

    def draw_rect(self, rect, color, text=None, text_color=WHITE):
        pygame.draw.rect(self.screen, color, rect)
        if text is not None:
            self.draw_text(text, text_color, rect.center)

    def draw_cell(self, maze, x, y, start_state, end_state):
        rect = pygame.Rect(get_rect(x, y, self.cell_size))
        pygame.draw.rect(self.screen, CELL_COLORS[maze.grid[y, x]], rect)
        if maze[x, y] == Cell.ENTRANCE:
            self.draw_text(start_state, WHITE, rect.center)
        elif maze[x, y] == Cell.EXIT:
            self.draw_text(end_state, WHITE, rect.center)
        elif maze[x, y] not in [Cell.NONE, Cell.WALL]:
            self.draw_text(maze[x, y], WHITE, rect.center)

    def draw_maze(self, maze, start_state, end_state):
        for y in range(maze.height):
            for x in range(maze.width):
                self.draw_cell(maze, x, y, start_state, end_state)

    def draw_player(self, maze, player, current_state):
        rect = pygame.Rect(get_rect(player.x, player.y, self.cell_size))
        if maze[player] == Cell.NONE:
            self.draw_rect(rect, CELL_COLORS[Cell.NONE], current_state, BLACK)
        pygame.draw.rect(self.screen, BLACK, rect, 3)
        return rect

    def draw_game(self, game, current_state):
        self.draw_maze(game.maze, game.level.start_state, game.level.end_state)
        rect = self.draw_player(game.maze, game.player, current_state)
        pygame.display.update()
        return rect

    def render_welcome(self):
        w, h = self.screen.get_width(), self.screen.get_height()
        self.screen.fill(WHITE)
        self.draw_text(TITLE_TEXT, BLACK, (0.5 * w, 0.25 * h), True)
        self.draw_text(CONTROLS_TEXT, BLACK, (0.5 * w, 0.45 * h))
        self.draw_text(NAVIGATION_TEXT, BLACK, (0.5 * w, 0.55 * h))
        self.draw_text(CONTINUE_TEXT, BLACK, (0.5 * w, 0.75 * h))
        pygame.display.update()

    def render_end(self):
        w, h = self.screen.get_width(), self.screen.get_height()
        self.screen.fill(WHITE)
        self.draw_text(END_TEXT, BLACK, (0.5 * w, 0.25 * h), True)
        self.draw_text(RESTART_TEXT, BLACK, (0.5 * w, 0.45 * h))
        # self.draw_text(NAVIGATION_TEXT, BLACK, (0.5 * w, 0.55 * h))
        self.draw_text(CONTINUE_TEXT, BLACK, (0.5 * w, 0.75 * h))
        pygame.display.update()

    def render_banner(self, header, title):
        w, h = self.screen.get_width(), self.screen.get_height()
        self.screen.fill(WHITE)
        self.draw_text(header, (0, 0, 0), (0.5 * w, 0.25 * h), True)
        self.draw_text(title, (0, 0, 0), (0.5 * w, 0.4 * h))
        self.draw_text(CONTINUE_TEXT, (0, 0, 0), (0.5 * w, 0.75 * h))
        pygame.display.update()


def get_rect(x, y, cell_size):
    return x * cell_size, y * cell_size, cell_size, cell_size
