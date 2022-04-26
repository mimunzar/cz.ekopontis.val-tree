#!/usr/bin/env python3

import src.val_tree.gateways.measurements as measurements


def test_not_empty():
    assert  measurements.not_empty([])        == False
    assert measurements.not_empty([None])     == False
    assert measurements.not_empty([42])       == True
    assert measurements.not_empty([None, 42]) == True

