#!/usr/bin/env python3

import src.val_tree.util as util


def test_drop():
    assert list(util.drop(None, [1, 2, 3])) == [1, 2, 3]
    assert list(util.drop(1,    [1, 2, 3])) == [2, 3]
    assert list(util.drop(2,    [1, 2, 3])) == [3]
    assert list(util.drop(42,   []))        == []

