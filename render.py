import pygame

from cell import CELL_COLORS
from maze import Cell

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CURRENT_STATE_COLOR = (150, 150, 150)


class Render():
    def __init__(self, screen, cell_size, font):
        self.screen = screen
        self.cell_size = cell_size
        self.font = font

    def draw_text(self, text, color, center):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=center)
        self.screen.blit(text_surface, text_rect)

    def draw_rect(self, rect, color, text=None, text_color=WHITE):
        pygame.draw.rect(self.screen, color, rect)
        if text is not None:
            self.draw_text(text, text_color, rect.center)

    def draw_cell(self, maze, x, y, rect, start_state, end_state):
        pygame.draw.rect(self.screen, CELL_COLORS[maze.grid[y, x]], rect)

        if maze.grid[y, x] == Cell.ENTRANCE:
            self.draw_text(start_state, WHITE, rect.center)
        elif maze.grid[y, x] == Cell.EXIT:
            self.draw_text(end_state, WHITE, rect.center)
        elif maze.grid[y, x] not in [Cell.NONE, Cell.WALL]:
            self.draw_text(maze.grid[y, x], WHITE, rect.center)

    def render_cell(self, maze, x, y, start_state, end_state):
        rect = pygame.Rect(get_rect(x, y, self.cell_size))
        self.draw_cell(maze, x, y, rect, start_state, end_state)

    def render_maze(self, maze, start_state, end_state):
        for y in range(maze.height):
            for x in range(maze.width):
                self.render_cell(maze, x, y, start_state, end_state)

    def render_player(self, maze, player, current_state):
        rect = pygame.Rect(get_rect(player.x, player.y, self.cell_size))
        if maze[player] == Cell.NONE:
            self.draw_rect(rect, CELL_COLORS[Cell.NONE], current_state, CURRENT_STATE_COLOR)
        pygame.draw.rect(self.screen, BLACK, rect, 3)
        return rect

    def render_game(self, game, start_state, end_state, current_state):
        self.render_maze(game.maze, start_state, end_state)
        rect = self.render_player(game.maze, game.player, current_state)
        return rect


def get_rect(x, y, cell_size):
    return x * cell_size, y * cell_size, cell_size, cell_size
