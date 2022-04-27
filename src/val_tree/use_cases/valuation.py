#!/usr/bin/env python3


def valuate_tree(storage_gtw, valuations_gtw, tree):
    v = valuations_gtw.valuate_tree(tree)
    return storage_gtw.write_tree_valuation(tree, v)

