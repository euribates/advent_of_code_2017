#!/usr/bin/env python3

import six

from six.moves import StringIO

class Lexer:

    def __init__(self, stream=None, text=''):
        if text:
            self.stream = StringIO(text)
        else:
            self.stream = stream
        self.next = self._get_char()

    def _get_char(self):
        c = self.stream.read(1)
        if c == '!':
            self.stream.read(1)  # ignore escaped char
            c = self._get_char()
        return c

    def get_input(self):
        print('get_input called', end='')
        while self.next:
            result = self.next
            self.next = self._get_char()
            print("returns '{}'".format(result))
            return result
        return ''

    def __iter__(self):
        return self

    def __next__(self):
        c = self.get_input()
        if c:
            return c
        else:
            raise StopIteration()

_score = 0
_total_score = 0
_removed_garbage = 0

def reset_total_score():
    global _score, _total_score
    _total_score = 0
    _score = 0

def get_total_score():
    global _total_score
    return _total_score

def garbage(lexer):
    global _removed_garbage
    print('garbage called')
    open_angle = lexer.get_input()
    assert open_angle == '<'
    while lexer.next != '>':
        lexer.get_input()
        _removed_garbage += 1
    close_angle = lexer.get_input()
    assert close_angle == '>'


def item(lexer):
    print('item called')
    if lexer.next == '{':
        group(lexer)
    elif lexer.next == '<':
        garbage(lexer)
    else:
        raise ValueError("Expected '<' or '}}', got '{}'".format(lexer.next))

def items(lexer):
    print('items called')
    item(lexer)
    while lexer.next == ',':
        lexer.get_input()
        item(lexer)

def group(lexer):
    global _score, _total_score
    print('group called')
    assert lexer.next == '{'
    open_key = lexer.get_input()
    _score += 1
    _total_score += _score
    assert open_key == '{'
    if lexer.next != '}':  #  not empty group
        items(lexer)
    close_key = lexer.get_input()
    assert close_key == '}'
    _score -= 1

if __name__ == '__main__':
    reset_total_score()
    with open('data.txt') as f:
        lexer = Lexer(stream=f)
        group(lexer)
        print('Total score:', get_total_score())
        print('Removed garbage:', _removed_garbage)
