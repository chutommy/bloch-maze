import pygame

from cell import CELL_COLORS
from maze import Cell

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CURRENT_STATE_COLOR = (150, 150, 150)


def get_rect(x, y, cell_size):
    return x * cell_size, y * cell_size, cell_size, cell_size


def draw_text(screen, text, color, center):
    seguisy50 = pygame.font.Font("seguisym.ttf", 25)
    text_surface = seguisy50.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    screen.blit(text_surface, text_rect)


def draw_rect(screen, rect, color, text=None, text_color=WHITE):
    pygame.draw.rect(screen, color, rect)
    if text is not None:
        draw_text(screen, text, text_color, rect.center)


def draw_cell(screen, maze, x, y, rect, start_state, end_state):
    pygame.draw.rect(screen, CELL_COLORS[maze.grid[y, x]], rect)
    if maze.grid[y, x] == Cell.ENTRANCE:
        draw_text(screen, start_state, WHITE, rect.center)
    elif maze.grid[y, x] == Cell.EXIT:
        draw_text(screen, end_state, WHITE, rect.center)
    elif maze.grid[y, x] not in [Cell.NONE, Cell.WALL]:
        draw_text(screen, maze.grid[y, x], WHITE, rect.center)


def render_cell(screen, maze, x, y, cell_size, start_state, end_state):
    rect = pygame.Rect(get_rect(x, y, cell_size))
    draw_cell(screen, maze, x, y, rect, start_state, end_state)


def render_maze(screen, maze, cell_size, start_state, end_state):
    for y in range(maze.height):
        for x in range(maze.width):
            render_cell(screen, maze, x, y, cell_size, start_state, end_state)


def render_player(screen, maze, player, cell_size, current_state):
    rect = pygame.Rect(get_rect(player.x, player.y, cell_size))
    if maze[player] == Cell.NONE:
        draw_rect(screen, rect, CELL_COLORS[Cell.NONE], current_state, CURRENT_STATE_COLOR)
    pygame.draw.rect(screen, BLACK, rect, 3)
    return rect


def render_game(screen, game, cell_size, start_state, end_state, current_state):
    render_maze(screen, game.maze, cell_size, start_state, end_state)
    rect = render_player(screen, game.maze, game.player, cell_size, current_state)
    return rect
