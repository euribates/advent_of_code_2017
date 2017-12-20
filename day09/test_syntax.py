#!/usr/bin/env python3

from solution import (
    Lexer, garbage, group,
    item, items,
    get_total_score, reset_total_score,
    )
import pytest


def test_empty_garbage():
    lexer = Lexer(text='<>')
    assert lexer.next == '<'
    garbage(lexer)

def test_garbage_random_characacters():
    lexer = Lexer(text='<random characters>')
    garbage(lexer)

def test_garbage_many_open_angle():
    lexer =  Lexer(text='<<<<>')
    garbage(lexer)

def test_garbage_ignore_open_angle():
    lexer = Lexer(text='<{!>}>')
    garbage(lexer)

def test_garbage_ignore_double_admonition():
    lexer = Lexer(text='<!!>')
    garbage(lexer)

def test_garbage_ignore_double_admon_and_angle():
    lexer = Lexer(text='<!!!>>')
    garbage(lexer)

def test_garbage_ignore_open_angle_and_trash():
    lexer = Lexer(text='<{o"i!a,<{i<a>')
    garbage(lexer)

# Groups

def test_empty_group():
    lexer = Lexer(text='{}')
    assert lexer.next == '{'
    group(lexer)

# Items

def get_score(text):
    reset_total_score()
    lexer = Lexer(text=text)
    items(lexer)
    return get_total_score()

def test_item_one_group():
    assert get_score('{}') == 1

def test_item_two_group():
    assert get_score('{{}}') == 3

def test_item_three_group():
    assert get_score('{{{}}}') == 6

def test_items_sum_five():
    assert get_score('{{},{}}') ==5

def test_items_sum_sixteen():
    assert get_score('{{{},{},{{}}}}') == 16

def test_items_four_garbages():
    assert get_score('{<a>,<a>,<a>,<a>}') == 1

def test_items_four_ab_mode_1():
    assert get_score('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9

def test_items_four_ab_mode_2():
    assert get_score('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9

def test_trick():
    assert get_score('{{<!>},{<!>},{<!>},{<a>}}') == 3

def test_trick_2():
    assert get_score('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3

def test_item_garbage():
    reset_total_score()
    lexer = Lexer(text='<5v5r7r5rv>')
    items(lexer)
    assert get_total_score() == 0

# list of items

def test_list_of_inputs():
    lexer = Lexer(text='{},<nahjb>,{},{<ip>}')
    items(lexer)
    assert get_total_score() == 3


if __name__ == '__main__':
    pytest.main()
