#!/usr/bin/env python3


def valuate_tree(valuations_gtw, storage_gtw, tree):
    val = valuations_gtw.valuate_tree(tree)
    return storage_gtw.write_tree_valuation(tree, val)

