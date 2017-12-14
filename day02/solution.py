#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

with open('data.txt', 'r') as f:
    lines = f.readlines()

mat = [
    [int(x) for x in line.split()]
    for line in lines
    ]

maximos = [ max(row) for row in mat]
minimos = [ min(row) for row in mat]
deltas = [maximo-minimo for (minimo, maximo) in zip(minimos, maximos)]
print('Part one', end=': ')
print(sum(deltas))

# test
# mat = [ [5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5] ]

acc = []
for row in mat:
    for (a,b) in itertools.permutations(row, 2):
        maximo, minimo = max(a, b), min(a, b)
        if maximo % minimo == 0:
            acc.append(maximo // minimo)
            break
print('Part two', end=': ')
print(sum(acc))


