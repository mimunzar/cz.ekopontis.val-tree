#!/usr/bin/env python3

import argparse
import functools as ft
import os
import sys

import src.val_tree.adapters.http as http_adp
import src.val_tree.adapters.excell as excell_adp
import src.val_tree.gateways.measurements as measurements_gtw
import src.val_tree.gateways.valuations as valuation_gtw
import src.val_tree.presenters.trees as tree_pre
import src.val_tree.use_cases.valuation as valuation
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

    valuate_tree = ft.partial(valuation.valuate_tree,
        valuation_gtw.make(args['reg_sec'], http_adp.make()),
        tree_pre     .make(output_sheet))

    #util.dorun(
    #  map(print_progress
    result = tuple(map(valuate_tree, util.take(2, measurements_gtw.iter_trees(input_sheet))))
    #      ))

    output_sheet.save()

