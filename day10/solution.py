#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

LIST_SIZE = 256

l = list(range(LIST_SIZE))
current_pos = 0
skip_size = 0
lengths = [3, 4, 1, 5]

def get_range(start, length):
    counter = length
    index = start
    while counter > 0:
        yield index
        index += 1
        if index >= LIST_SIZE:
            index = 0
        counter -= 1


def extract_sublist(current_pos, length):
    return [l[i] for i in get_range(current_pos, length)]

def replace_sublist(current_pos, length, sublist):
    for i1, i2 in enumerate(get_range(current_pos, length)):
        l[i2] = sublist[i1]

def debug():
    global l
    buff = []
    for i, n in enumerate(l):
        if i == current_pos:
            buff.append('[{}]'.format(n))
        else:
            buff.append(str(n))
    return ', '.join(buff)


current_pos = 0
skip_size = 0


# tests
# lengths = [3, 4, 1, 5]
# assert list(get_range(0, 3)) == [0, 1, 2]
# assert list(get_range(3, 4)) == [3, 4, 0, 1]

lengths = [157,222,1,2,177,254,0,228,159,140,249,187,255,51,76,30]

for length in lengths:
    sublist = extract_sublist(current_pos, length)
    sublist.reverse()
    replace_sublist(current_pos, length, sublist)
    current_pos = (current_pos + (length + skip_size)) % LIST_SIZE 
    skip_size += 1
print('Part 1')
print(l[0]*l[1])


print('Part 2')

def str_to_lengths(s):
    return [ord(c) for c in s] + [17, 31, 73, 47, 23]

# tests
str_to_lengths('123') == [49,44,50,44,51,17,31,73,47,23]

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


lengths = str_to_lengths('AoC 2017')
l = list(range(LIST_SIZE))
current_pos = 0
skip_size = 0
for _ in range(64):
    lengths = str_to_lengths('AoC 2017')
    for length in lengths:
        sublist = extract_sublist(current_pos, length)
        sublist.reverse()
        replace_sublist(current_pos, length, sublist)
        current_pos = (current_pos + (length + skip_size)) % LIST_SIZE 
        skip_size += 1

dense_hash = sparse_to_dense(l)
print(dense_hash)
print(as_hexa(dense_hash))

print('Sol 2:')
l = list(range(LIST_SIZE))
current_pos = 0
skip_size = 0
for _ in range(64):
    lengths = str_to_lengths('157,222,1,2,177,254,0,228,159,140,249,187,255,51,76,30')
    for length in lengths:
        sublist = extract_sublist(current_pos, length)
        sublist.reverse()
        replace_sublist(current_pos, length, sublist)
        current_pos = (current_pos + (length + skip_size)) % LIST_SIZE 
        skip_size += 1

dense_hash = sparse_to_dense(l)
print(dense_hash)

print(as_hexa(dense_hash))
