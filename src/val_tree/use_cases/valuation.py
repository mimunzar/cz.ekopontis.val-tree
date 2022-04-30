#!/usr/bin/env python3


def valuate_tree(valuation_gtw, tree_pre, tree):
    return tree_pre.write_valuation(tree, valuation_gtw.valuate_tree(tree))

