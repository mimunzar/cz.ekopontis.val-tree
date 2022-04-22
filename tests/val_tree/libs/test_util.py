#!/usr/bin/env python3

import pytest
import src.val_tree.libs.util as util


def test_take():
    assert list(util.take(None, [1, 2, 3])) == [1, 2, 3]
    assert list(util.take(0,    [1, 2, 3])) == []
    assert list(util.take(2,    [1, 2, 3])) == [1, 2]
    assert list(util.take(42,   [1, 2, 3])) == [1, 2, 3]


def test_drop():
    assert list(util.drop(None, [1, 2, 3])) == [1, 2, 3]
    assert list(util.drop(1,    [1, 2, 3])) == [2, 3]
    assert list(util.drop(2,    [1, 2, 3])) == [3]
    assert list(util.drop(42,   []))        == []


def test_first():
    with pytest.raises(StopIteration):
        util.first([])
    assert util.first([1, 2])       == 1
    assert util.first(iter([1, 2])) == 1


def test_nth():
    with pytest.raises(StopIteration):
        util.nth(2, [])
    assert util.nth(0, [1, 2, 3])       == 1
    assert util.nth(2, iter([1, 2, 3])) == 3


def test_second():
    with pytest.raises(StopIteration):
        util.second([])
    assert util.second([1, 2])       == 2
    assert util.second(iter([1, 2])) == 2


def test_pluck():
    with pytest.raises(KeyError):
        util.pluck(['baz'], {'foo': 42, 'bar': 43})
    with pytest.raises(TypeError):
        util.pluck([], {'foo': 42, 'bar': 43})
    assert util.pluck(['foo'],        {'foo': 42, 'bar': 43}) == 42
    assert util.pluck(['foo', 'bar'], {'foo': 42, 'bar': 43}) == (42, 43)


def test_complement():
    assert util.complement(lambda: True)()  == False
    assert util.complement(lambda: False)() == True
    assert util.complement(lambda i: 0 == i % 2)(1) == True
    assert util.complement(lambda i: 0 == i % 2)(2) == False


def test_compose():
    neg = lambda x: not x
    inc = lambda x: x + 1
    assert util.compose(lambda: True)()           == True
    assert util.compose(neg, lambda: True)()      == False
    assert util.compose(neg, neg, lambda: True)() == True
    assert util.compose(inc, inc, inc, inc)(0)    == 4


def test_any_fn():
    is_zero = lambda x: 0 == x
    is_one  = lambda x: 1 == x
    assert util.any_fn(lambda: False)()               == False
    assert util.any_fn(lambda: False, lambda: True)() == True
    assert util.any_fn(is_zero, is_one)(1)            == True


def test_partition_by():
    is_odd = lambda x: x % 2
    assert list(map(list, util.partition_by(is_odd, [])))        == [[], []]
    assert list(map(list, util.partition_by(is_odd, [1])))       == [[1], []]
    assert list(map(list, util.partition_by(is_odd, [1, 2])))    == [[1], [2]]
    assert list(map(list, util.partition_by(is_odd, [1, 2, 3]))) == [[1, 3], [2]]


def test_make_validator():
    assert util.make_validator('Fail', lambda: False)()    == (False, 'Fail')
    assert util.make_validator('Fail', lambda: True)()     == (True,  'Fail')
    assert util.make_validator('Fail', lambda x: x % 2)(1) == (True,  'Fail')


def test_make_checker():
    checker = util.make_checker({
        'foo': util.make_validator('Failed foo', lambda x: x > 0),
        'bar': util.make_validator('Failed bar', lambda x: x > 0),
    })
    assert checker({'foo': 0, 'bar': 0, 'baz': 0}) == ('Failed foo', 'Failed bar',)
    assert checker({'foo': 0, 'bar': 1, 'baz': 0}) == ('Failed foo',)
    assert checker({'foo': 1, 'bar': 1, 'baz': 0}) == tuple()


def test_make_ravg():
    ravg = util.make_ravg()
    assert ravg(0) == 0
    assert ravg(2) == 1
    assert ravg(4) == 2
    assert ravg(6) == 3
    assert ravg(8) == 4

