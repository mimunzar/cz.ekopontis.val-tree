#!/usr/bin/env python3

import pytest

import src.val_tree.entities.tree_est as tree_est


def test_from_response():
    with pytest.raises(KeyError):
        tree_est.from_response({})
    with pytest.raises(ValueError):
        tree_est.from_response({'value_in_czk': -42})
    assert tree_est.from_response({'value_in_czk': 42}) == {'value_czk': 42}

