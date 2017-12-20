#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

_map = {}

class Node:

    def __init__(self, name, weight):
        if name not in _map:
            _map[name] = self
        self.name = name
        self.weight = weight
        self.sons = []
        self.parent = ''

    def debug(self):
        buff = [self.name]
        buff.append(' - weight: {}'.format(repr(self.weight)))
        buff.append(' - sons: {}'.format(repr(self.sons)))
        buff.append(' - parent: {}'.format(repr(self.parent)))
        return '\n'.join(buff)

    def __str__(self):
        buff = ['{} ({})'.format(self.name, self.weight)]
        if self.sons:
            buff.append(' -> ')
            buff.append(', '.join(self.sons))
        buff.append(' [Parent is "{}"]'.format(self.parent))
        return ''.join(buff)

with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f if l.strip()]

pat_l = re.compile('([a-z]+) \((\d+)\)(.*)')

for l in lines:
    m = pat_l.match(l)
    if  m:
        name = m.group(1)
        weight = int(m.group(2))
        nodo = Node(name, weight)
        resto = m.group(3)
        if resto:
            assert resto.startswith(' -> ')
            resto = resto[4:]
            sons = [s.strip() for s in resto.split(', ')]
            for son in sons:
                nodo.sons.append(son)
    else:
        print('linea "{}" no casa'.format(l))
        break
else:
    print('Todo ok')

for name in _map:
    node = _map[name]
    if node.sons:
        for son_name in node.sons:
            son_node = _map[son_name]
            son_node.parent = name

for name in _map:
    node = _map[name]
    if node.parent == '':
        root = node
        print('root is {}'.format(node.name))
        break

# part 2

def total_weight(node):
    acc = node.weight
    for son_name in node.sons:
        son = _map[son_name]
        acc += total_weight(son)
    return acc

def trace(node_name):
    node = _map[node_name]
    print('{} weight is {}'.format(node.name, node.weight))
    print('{} total weight is '.format(node.name, total_weight(node)))
    for son_name in node.sons:
        son = _map[son_name]
        print('  - {} total weight is {}'.format(son.name, total_weight(son)))

trace('vvsvez')
trace('nbyij')
trace('tdxow')
trace('ghwgd')
