#!/usr/bin/env python3

import argparse
import functools as ft
import os
import sys

import src.val_tree.adapters.http as http_adp
import src.val_tree.adapters.excell as excell_adp
import src.val_tree.gateways.tree_dat as tree_dat
import src.val_tree.gateways.ochranaprirody as ochranaprirody
import src.val_tree.presenters.tree_est as tree_est
import src.val_tree.use_cases.valuate_tree as valuate_tree
import src.val_tree.libs.util as util


def parse_args(args_it):
    parser = argparse.ArgumentParser()
    parser.add_argument('input-sheet', help='The input Excell sheet with measurements',
            metavar='FILE')
    parser.add_argument('--reg-sec',   help='The number of valuated items per second',
            required=False, metavar="NUM", default=2)
    return vars(parser.parse_args(args_it))


def output_path(fpath):
    path, ext = os.path.splitext(fpath)
    return f'{path}.val{ext}'


if '__main__' == __name__:
    args         = parse_args(sys.argv[1:])
    input_sheet  = excell_adp.make(args['input-sheet'])
    output_sheet = excell_adp.make(output_path(args['input-sheet']))

    # filter(lambda x: isinstance(x, int),
    #         output_sheet.wb.active.iter_cols(min_col=1, max_col=1, values_only=True))

    tree_est = tree_est.make(output_sheet)
    val_tree = ft.partial(valuate_tree.valuate,
        ochranaprirody.make(args['reg_sec'], http_adp.make()), tree_est)

    #util.dorun(
    #  map(print_progress
    result = tuple(map(val_tree, util.take(2, tree_dat.iter_trees(input_sheet))))
    #      ))

    tree_est.write_footer()
    output_sheet.save()

