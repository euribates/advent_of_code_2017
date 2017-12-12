#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node:

    _map = {}

    @staticmethod
    def get(id_node):
        if id_node not in Node._map:
            node = Node(id_node)
            Node._map[id_node] = node
        return Node._map[id_node]

    def __init__(self, id_node):
        assert id_node not in Node._map
        self.id_node = id_node
        self.links = set([])

    def link(self, other):
        self.links.add(other)
        other.links.add(self)

    def __str__(self):
        return 'Node {} links to: {}'.format(
            self.id_node,
            ', '.join([str(n.id_node) for n in self.links])
            )

def create_node(l):
    (id_node, neighbours) = l.split(' <-> ')
    id_node = int(id_node)
    node = Node.get(id_node)
    links = [int(l.strip()) for l in neighbours.split(',')]
    for id_neighbour in links:
        node.link(Node.get(id_neighbour))

# with open('input_test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    for line in f:
        create_node(line.strip())

def reachables_from(id_node):
    group = set()
    to_visit = set([id_node])
    while to_visit:
        id_node = to_visit.pop()
        group.add(id_node)
        # print('Visiting {}'.format(id_node))
        node = Node.get(id_node)
        for son in node.links:
            #  print(' - links to {}'.format(son))
            if son.id_node not in group:
                to_visit.add(son.id_node)
    return group

root = Node.get(0)
root_reachables = reachables_from(0)

print('Root:', root)
print('Part 1:', len(root_reachables))

## Part tow

all_nodes = Node._map.keys()
groups = dict()
seen_nodes = set([])
for id_node in all_nodes:
    if id_node in seen_nodes:
        continue
    node = Node.get(id_node)
    reachables = reachables_from(id_node)
    seen_nodes.add(id_node)
    seen_nodes.update(reachables)
    id_group = min(reachables)
    groups[id_group] = list(reachables)

print('Part 2:', len(groups))

# Extra: generate graphviz

linked = set([])
root = 214
with open('grafo.dot', 'w') as f:
    f.write('graph {\n')
    f.write('  rankdir=TB;\n')
    f.write('  {}[shape=doublecircle];'.format(root))
    node = Node.get(root)
    reachables = reachables_from(root)
    f.write('  {} -- {{ {} }}[color=red,penwidth=3.0];\n'.format(
        node.id_node, 
        ', '.join([str(n.id_node) for n in node.links]),
        ))
    for n in node.links:
        linked.add( (node.id_node, n.id_node) )
        linked.add( (n.id_node, node.id_node) )

    for id_node in reachables:
        node = Node.get(id_node)
        links = []
        for n in node.links:
            t1 = (id_node, n.id_node)
            t2 = (n.id_node, id_node)
            if t1 not in linked and t2 not in linked:
                links.append(n.id_node)
                linked.add(t1)
                linked.add(t2)
        f.write('  {} -- {{ {} }};\n'.format(
            node.id_node, 
            ', '.join([str(n) for n in links]),
            ))
    f.write('}')

