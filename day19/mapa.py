#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum

def chop(l):
    if ord(l[-1]) == 10:
        l = l[:-1]
    return l

with open('input.txt', 'r') as f:
    lines = [chop(l) for l in f.readlines()]

linemap = []
for l in lines:
    linemap.append(list(l))

max_rows = len(linemap)
max_cols = len(linemap[0])


def char_at_pos(row, col):
    global linemap, max_rows, max_width
    if (0 <= row < max_rows) and (0 <= col < max_cols):
        return linemap[row][col]
    else:
        return None

class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 4
    WEST = 8

    def oposite(d):
        _map_oposites = {
            Direction.NORTH: Direction.SOUTH,
            Direction.SOUTH: Direction.NORTH,
            Direction.EAST: Direction.WEST,
            Direction.WEST: Direction.EAST,
            }
        return _map_oposites[d]

# test
assert Direction.oposite(Direction.NORTH) == Direction.SOUTH
assert Direction.oposite(Direction.SOUTH) == Direction.NORTH
assert Direction.oposite(Direction.EAST) == Direction.WEST
assert Direction.oposite(Direction.WEST) == Direction.EAST


def south(pos): return pos[0]+1, pos[1]
def north(pos): return pos[0]-1, pos[1]
def east(pos): return pos[0], pos[1]+1
def west(pos): return pos[0], pos[1]-1

# test
test_pos = (5, 9)
assert south(test_pos) == (6, 9)
assert north(test_pos) == (4, 9)
assert east(test_pos) == (5, 10)
assert west(test_pos) == (5, 8)


def print_map(m):
    for line in m:
        for c in line:
            print(c, end='')
        print()


def next_pos(direction, pos):
    _map_calls = {
        Direction.NORTH: north,
        Direction.EAST: east,
        Direction.SOUTH: south,
        Direction.WEST: west,
        }
    return _map_calls[direction](pos)

def find_new_direction(direction, pos):
    row, col = pos
    possible_directions = set(Direction)
    possible_directions.discard(Direction.oposite(direction))  # No way back
    for new_dir in possible_directions:
        r, c = next_pos(new_dir, pos)
        c = char_at_pos(r, c)
        if c is None:
            continue
        if c in '-|+ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            break
    else:
        raise ValueError('No puedo seguir')
    return new_dir

direction = Direction.SOUTH
row = 0
col = linemap[0].index('|')
pos = (row, col)
assert linemap[row][col] == '|'

found_letters = []

counter = 0
while True:
    row, col = pos
    c = linemap[row][col]
    print('pos {},{} encuentro char {}'.format(row, col, c), end=' ')
    
    if c == ' ':
        print('Encontrado')
        print('found_letters:', ''.join(found_letters))
        print('steps:', counter)
        break

    if c == '+':
        direction = find_new_direction(direction, pos)
        print('Cambio direccion: {}'.format(direction), end=' ')
        pos = next_pos(direction, pos)
        counter += 1

    elif c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print('Añado letra "{}"'.format(c), end=' ')
        found_letters.append(c)
        pos = next_pos(direction, pos)
        counter += 1
    elif c == '|':
        pos = next_pos(direction, pos)
        counter += 1
    elif c == '-':
        pos = next_pos(direction, pos)
        counter += 1
    print('me dirijo a nueva pos', pos)
