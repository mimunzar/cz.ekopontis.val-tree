#!/usr/bin/env python3

import src.val_tree.gateways.tree_dat as tree_dat


def test_not_empty():
    assert tree_dat.not_empty([])         == False
    assert tree_dat.not_empty([None])     == False
    assert tree_dat.not_empty([42])       == True
    assert tree_dat.not_empty([None, 42]) == True

