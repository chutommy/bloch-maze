import sys
import time

import pygame

from game import Game, GameState
from level import Level
from maze import Maze
from render import render_game, render_cell, render_player
from state import State

m = Maze([
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', '.'],
    ['.', 'w', 'A', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'w', '.'],
    ['.', 'w', '.', '.', 'X', '.', 'H', '.', 'S', '.', '0', '.', '.', '.', '.', 'w', '.'],
    ['.', 'w', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'w', '.'],
    ['.', 'w', '.', '.', 'Y', '.', 'Z', '.', 'S†', '.', '1', '.', '.', '.', '.', 'w', '.'],
    ['.', 'w', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', 'w', '.'],
    ['.', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
])

b = State.ONE
lvl = Level(m, b, b)
game = Game(lvl)

CELL_SIZE = 50
SCREEN_WIDTH = game.maze.grid.shape[1] * CELL_SIZE
SCREEN_HEIGHT = game.maze.grid.shape[0] * CELL_SIZE
FPS = 60
DELAY = 0.08

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bloch's Maze")
clock = pygame.time.Clock()

oldRect = render_game(screen, game, CELL_SIZE, lvl.start_state, lvl.end_state, lvl.start_state)
pygame.display.flip()

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if game.state == GameState.SUCCESS:
        running = False
    elif game.state == GameState.FAIL:
        game.reset()
        oldRect = render_game(screen, game, CELL_SIZE, lvl.start_state, lvl.end_state, lvl.start_state)
        pygame.display.flip()

    prev = game.player
    key = pygame.key.get_pressed()
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
        time.sleep(DELAY)
    else:
        continue

    render_cell(screen, game.maze, prev.x, prev.y, CELL_SIZE, lvl.start_state, lvl.end_state)
    newRect = render_player(screen, game.maze, game.player, CELL_SIZE, game.player_state)
    pygame.display.update(oldRect)
    pygame.display.update(newRect)
    oldRect = newRect

pygame.quit()
sys.exit()
