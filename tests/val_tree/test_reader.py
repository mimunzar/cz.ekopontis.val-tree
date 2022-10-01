#!/usr/bin/env python3

import src.val_tree.parser as parser


def test_read_tree_radiuses():
    assert parser.read_tree_radiuses('')                          == tuple()
    assert parser.read_tree_radiuses('106')                       == ()
    assert parser.read_tree_radiuses('stromořadí nad 10 stromů')  == ()
    assert parser.read_tree_radiuses('dvojkmen: 106;109')         == (106, 109)
    assert parser.read_tree_radiuses('čtyřkmen: 49;87;87;99')     == (49, 87, 87, 99)

