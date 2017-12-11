#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Vector:
    
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        
    def __str__(self):
        return "<{}, {}, {}>".format(self.x, self.y, self.z)
        
    def __repr__(self):
        return "Vector({}, {}, {})".format(self.x, self.y, self.z)
 
    def __len__(self):
        return max(abs(self.x), abs(self.y), abs(self.z))

# Initial vectors

center = Vector(0,0, 0)

n = Vector(x=0, y=1, z=-1)
s = Vector(x=0, y=-1, z=1)

ne = Vector(x=1, y=0, z=-1)
sw = Vector(x=-1, y=0, z=1)

se = Vector(x=1, y=-1, z=0)
nw = Vector(x=-1, y=1, z=0)

# tests

assert len(ne + ne + ne) == 3

assert len(ne + ne + sw + sw) == 0

assert len(ne + ne + s + s) == 2

assert len(se + sw + se + sw + sw) == 3

with open('input.txt', 'r') as f:
    path = [_.strip() for _ in f.read().split(',')]

print('Path:', path[0:5], '...', path[-5:])

map_steps = {
    'n': lambda v: v+n,
    's': lambda v: v+s,
    'sw': lambda v: v+sw,
    'ne': lambda v: v+ne,
    'se': lambda v: v+se,
    'nw': lambda v: v+nw,
}

maximo = -57892752
start = pos = Vector(0, 0, 0)
for step in path:
    pos = map_steps[step](pos)
    if len(pos) > maximo:
        maximo = len(pos)

print('Part 1: ', len(pos))
print('Part 2:', maximo)

