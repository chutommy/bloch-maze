import sys

import pygame

from config import *
from game import Game, GameState
from level import get_levels
from render import Render

pygame.init()
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

levels, dimensions = get_levels()
width = dimensions[1] * CELL_SIZE
height = dimensions[0] * CELL_SIZE
screen = pygame.display.set_mode((width, height))
render = Render(screen, CELL_SIZE, pygame.font.SysFont(FONT, FONT_SIZE))


def wait_keypress():
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            break


render.welcome()
pygame.display.update()
pygame.time.wait(BANNER_DELAY)
pygame.event.clear()
wait_keypress()

render.banner(levels[0].title, levels[0].subtitle)
pygame.display.update()
pygame.time.wait(BANNER_DELAY)
pygame.event.clear()
wait_keypress()

game = Game(levels[0])
oldRect = render.game(game, game.level.start_state, game.level.end_state, game.level.start_state)
pygame.display.update()

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if game.state == GameState.SUCCESS:
        render.banner(f"successfully finished {levels[0].title}", 'well done!')
        pygame.display.update()
        wait_keypress()

        game = Game(levels[1])
        oldRect = render.game(game, game.level.start_state, game.level.end_state, game.level.start_state)
        pygame.display.update()
    elif game.state == GameState.FAIL:
        game.reset()
        oldRect = render.game(game, game.level.start_state, game.level.end_state, game.level.start_state)
        pygame.display.update()

    prev = game.player
    key = pygame.key.get_pressed()

    if key[pygame.K_r]:
        game.fail()
        continue

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
    else:
        continue

    render.cell(game.maze, prev.x, prev.y, game.level.start_state, game.level.end_state)
    newRect = render.player(game.maze, game.player, game.player_state)
    pygame.display.update(oldRect)
    pygame.display.update(newRect)
    oldRect = newRect

pygame.quit()
sys.exit()
