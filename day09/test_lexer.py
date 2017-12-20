#!/usr/bin/env python3

from solution import Lexer
import pytest

def test_lexer_next():
    lexer = Lexer(text='ABCD')
    assert lexer.next == 'A'
    c = lexer.get_input()
    assert c == 'A'
    assert lexer.next == 'B'

    c = lexer.get_input()
    assert c == 'B'
    assert lexer.next == 'C'

    c = lexer.get_input()
    assert c == 'C'
    assert lexer.next == 'D'

    c = lexer.get_input()
    assert c == 'D'
    assert lexer.next == ''

    c = lexer.get_input()
    assert c == ''


def test_lexer():
    lexer = Lexer(text='<<<<>')
    assert list(lexer) == ['<', '<', '<', '<', '>']

def test_lexer_first_angle_canceled():
    lexer = Lexer(text='<{!>}>')
    assert list(lexer) == ['<', '{', '}', '>']

def test_lexer_second_admonition_canceled():
    lexer = Lexer(text='<!!>')
    assert list(lexer) == ['<', '>']

def test_lexer_second_admonitio_first_angle_canceled():
    lexer = Lexer(text='<!!!>>')
    assert list(lexer) == ['<', '>']

def test_lexer_key_inside_garbage():
    lexer = Lexer(text='<{o"i!a,<{i<a>')
    assert ''.join(list(lexer)) == '<{o"i,<{i<a>'

if __name__ == '__main__':
    pytest.main()
