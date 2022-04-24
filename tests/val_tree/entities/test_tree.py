#!/usr/bin/env python3

import pytest

import src.val_tree.entities.tree as tree


def test_iter_names():
    assert list(tree.iter_names('foo|bar'))     == ['foo', 'bar']
    assert list(tree.iter_names('foo | bar'))   == ['foo', 'bar']
    assert list(tree.iter_names(' foo | bar ')) == ['foo', 'bar']


def test_iter_trunk_diameter():
    assert list(tree.iter_trunk_diameter(42))       == [42]
    assert list(tree.iter_trunk_diameter('42'))     == [42]
    assert list(tree.iter_trunk_diameter('42;43'))  == [42, 43]
    assert list(tree.iter_trunk_diameter('42;43;')) == [42, 43]
    assert list(tree.iter_trunk_diameter('42,43,')) == [42, 43]


def test_iter_habitats():
    with pytest.raises(KeyError):
        tree.iter_habitats(['foo'], ['a'], {})
    assert list(tree.iter_habitats(['foo'], ['a'], {'foo': None})) == []
    assert list(tree.iter_habitats(['foo'], ['a'], {'foo': 'a'}))  == ['foo']
    assert list(tree.iter_habitats(['foo', 'bar'],
        ['a', 'A'], {'foo': 'a', 'bar': 'A'})) == ['foo', 'bar']

