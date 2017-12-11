#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Part one is easy using sets

with open('input.txt', 'r') as f:
    count = 0
    for line in f:
        words = list(line.split())
        set_words = set(words)
        if len(words) == len(set_words):
            count+=1

print('part 1:', count)

def are_anagrams(s1, s2):
    letters_s1 = sorted(list(s1))
    letters_s2 = sorted(list(s2))
    # print(letters_s1, letters_s2)
    return letters_s1 == letters_s2

# tests

assert are_anagrams('abcde', 'ecdab') is True
assert are_anagrams('abcde', 'xyz') is False
assert are_anagrams('xyz', 'abcde') is False

def is_valid_password(s):
    words = s.split()
    num_words = len(words)
    for w in words:
        s = set(words[:])
        if num_words != len(s): # There are repeated words
            return False 
        s.discard(w)
        for w2 in s:
            if are_anagrams(w, w2):
                # print(w, w2)
                return False
    return True

assert is_valid_password('abcde xyz ecdab') is False
assert is_valid_password('a ab abc abd abf abj') is True
assert is_valid_password('iiii oiii ooii oooi oooo') is True
assert is_valid_password('oiii ioii iioi iiio') is False
assert is_valid_password('una nau') is False
assert is_valid_password('tclq ytw tclq tezcqys') is False
assert is_valid_password('una nau') is False
assert is_valid_password('una una') is False

with open('input.txt', 'r') as f:
    count = 0
    for (i, line) in enumerate(f):
        line = line.strip()
        # print('Line {}'.format(i), line, sep=':', end=':')
        if is_valid_password(line):
            count += 1
print('Part2:', count)
