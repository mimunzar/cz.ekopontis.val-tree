#!/usr/bin/env python3

import pytest

import src.val_tree.entities.valuation as valuation


def test_from_response():
    with pytest.raises(KeyError):
        valuation.from_response({})
    with pytest.raises(ValueError):
        valuation.from_response({'value_in_czk': -42})
    assert valuation.from_response({'value_in_czk': 42}) == {'value_czk': 42}

