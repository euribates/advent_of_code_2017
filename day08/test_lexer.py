#!/usr/bin/env python3

import six

from six.moves import StringIO

class Lexer:

    def __init__(self, stream=None, text=''):
        if text:
            self.stream = StringIO(text)
        else:
            self.stream = stream
        self.next = self.get_char()

    def get_char(self):
        c = self.stream.read(1)
        if c == '!':
            ignore = self.stream.read(1)
            c = self.get_char()
        return c

    def get_input(self):
        while self.next:
            result = self.next
            self.next = self.get_char()
            yield result
        return


lexer = Lexer(text='<<<<>')
assert list(lexer.get_input()) == ['<', '<', '<', '<', '>']

lexer = Lexer(text='<{!>}>')
assert list(lexer.get_input()) == ['<', '{', '}', '>'] # first > is canceled

lexer = Lexer(text='<!!>')
assert list(lexer.get_input()) == ['<', '>'] # second ! is canceled

lexer = Lexer(text='<!!!>>')
assert list(lexer.get_input()) == ['<', '>'] # second ! and first > canceled

lexer = Lexer(text='<{o"i!a,<{i<a>')
assert ''.join(list(lexer.get_input())) == '<{o"i,<{i<a>'



def garbage(lexer):
    open_angle = lexer.get_char(); assert open_angle == '<'
    c = lexer.get_char()
    while lexer.next != '>':
        c = self.get_char()
    close_angle = lexer.get_char(); assert clase_angle == '>'
    assert c == '>'
    return 0

assert garbage(Lexer(text='<>')) == 0
assert garbage(Lexer(text='<random characters>')) == 0
assert garbage(Lexer(text='<<<<>')) == 0
assert garbage(Lexer(text='<{!>}>')) == 0
assert garbage(Lexer(text='<!!>')) == 0
assert garbage(Lexer(text='<!!!>>')) == 0
assert garbage(Lexer(text='<{o"i!a,<{i<a>')) == 0


def group(lexer, counter=1):
    open_key = lexer.get_char();  assert open_key == '{'
    items(lexer)
    close_key = lexer.get_char();  assert close_key == '}'


