#!/usr/bin/env python3

import src.val_tree.entities.measurement as measurement
import src.val_tree.entities.tree as tree
import src.val_tree.libs.util as util


def not_empty(val_it):
    return any(val_it)


def iter_vals(col_it):
    return tuple(map(lambda c: c.value, col_it))


def iter_trees(excell_adp):
    tree_sheet = excell_adp.open_sheet('zaznam_stromy')
    row_it     = filter(not_empty, map(iter_vals, util.drop(1, tree_sheet.iter_rows())))
    return map(tree.from_measurement, map(measurement.from_row, row_it))

