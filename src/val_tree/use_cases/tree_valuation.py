#!/usr/bin/env python3


def make(valuations_gtw, storage_gtw):
    def valuate(tree):
        val = valuations_gtw.valuate_tree(tree)
        return storage_gtw.write_tree_valuation(tree, val)
    return valuate

