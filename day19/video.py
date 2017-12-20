#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import pygame
import random
import os
from mapa import load_map, char_at_pos, find_path

FPS = 70

PALE_GREEN = (33, 99, 33)
GREEN = (00, 255, 0)
WHITE = (255, 255, 255)

pygame.init()
size = width, height = 604, 604
black = 0, 0, 0

linemap = load_map()
max_rows = len(linemap)
max_cols = len(linemap[0])

screen = pygame.display.set_mode(size)

path = find_path()
def map_iter():
    global linemap, max_rows, max_cols
    for row in range(max_rows):
        for col in range(max_cols):
            yield(row, col)


def draw_cell(scr, row, col, c, color=PALE_GREEN, second_color=PALE_GREEN):
    if c == ' ':
        return
    x, y = col * 3, row * 3
    if c == '|':
        pygame.draw.line(scr, color, (x+1, y), (x+1, y+3), 1)
    elif c == '-':
        pygame.draw.line(scr, color, (x, y+1), (x+3, y+1), 1)
    elif c == '+':
        pygame.draw.line(scr, color, (x+1, y), (x+1, y+3), 1)
        pygame.draw.line(scr, color, (x, y+1), (x+3, y+1), 1)
    elif c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        pygame.draw.rect(scr, second_color, (x, y, 3, 3), 0)

if not os.path.isdir('frames'):
    os.mkdir('frames')

clock = pygame.time.Clock()
frame = 0
while True:
    frame += 1
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    counter = 0
    for row, col in map_iter():
        counter += 1
        draw_cell(screen, row, col, char_at_pos(row, col)) 
        #if counter > frame:
        #    break
    for pos in path[0:frame*24]:
        (row, col) = pos
        c = char_at_pos(row, col)
        draw_cell(screen, row, col, c, GREEN, WHITE)
    pygame.display.flip()
    pygame.image.save(screen, 'frames/AoC-d19-{:04d}.tga'.format(frame))
    if frame*24 > len(path):
        break

print(path)
