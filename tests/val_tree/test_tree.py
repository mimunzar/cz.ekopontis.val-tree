#!/usr/bin/env python3

import src.val_tree.tree as tree
import src.val_tree.util as util



def test_is_microhabitat():
    assert all(map(tree.is_microhabitat,                  ['a', 'A', 'y', 'Y', '1', True]))
    assert all(map(util.complement(tree.is_microhabitat), ['r', 'R', 'e', 'E']))


def test_is_ext_microhabitat():
    assert all(map(tree.is_ext_microhabitat,                  ['r', 'R', 'e', 'E']))
    assert all(map(util.complement(tree.is_ext_microhabitat), ['a', 'A', 'y', 'Y', '1', True]))


def test_iter_microhabitats():
    idata = {'foo': None}
    assert list(map(list, tree.iter_microhabitats(idata, idata.keys()))) == [
            [], []]
    idata = {'foo': None, 'bar': 'A'}
    assert list(map(list, tree.iter_microhabitats(idata, idata.keys()))) == [
            [('bar', 'A'),], []]
    idata = {'foo': None, 'bar': 'A', 'baz': 'A'}
    assert list(map(list, tree.iter_microhabitats(idata, idata.keys()))) == [
            [('bar', 'A'), ('baz', 'A'),], []]
    idata = {'foo': None, 'bar': 'A', 'baz': 'A', 'bax': 'R'}
    assert list(map(list, tree.iter_microhabitats(idata, idata.keys()))) == [
            [('bar', 'A'), ('baz', 'A'),], [('bax', 'R')]]

