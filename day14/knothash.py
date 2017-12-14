#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

LIST_SIZE = 256


def get_range(start, length):
    counter = length
    index = start
    while counter > 0:
        yield index
        index += 1
        if index >= LIST_SIZE:
            index = 0
        counter -= 1


def extract_sublist(l, current_pos, length):
    return [l[i] for i in get_range(current_pos, length)]


def replace_sublist(l, current_pos, length, sublist):
    for i1, i2 in enumerate(get_range(current_pos, length)):
        l[i2] = sublist[i1]


def str_to_lengths(s):
    return [ord(c) for c in s] + [17, 31, 73, 47, 23]


def sparse_to_dense(l):
    assert len(l) == 256
    buff = []
    for index in range(0, 256, 16):
        buff.append(reduce(lambda x,y: x ^ y, l[index:index+16]))
    return buff

def as_hexa(l):

    def hexa(n):
        s = hex(n)[2:]
        if len(s) < 2:
            s = '0' + s
        return s

    assert len(l) == 16
    return ''.join([hexa(_) for _ in l])

def hash_as_hexa(s):
    lengths = str_to_lengths(s)
    l = list(range(LIST_SIZE))
    current_pos = 0
    skip_size = 0
    for _ in range(64):
        lengths = str_to_lengths(s)
        for length in lengths:
            sublist = extract_sublist(l, current_pos, length)
            sublist.reverse()
            replace_sublist(l, current_pos, length, sublist)
            current_pos = (current_pos + (length + skip_size)) % LIST_SIZE 
            skip_size += 1
    dense_hash = sparse_to_dense(l)
    return as_hexa(dense_hash)
