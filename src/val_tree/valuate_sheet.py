#!/usr/bin/env python3

import argparse
import functools as ft
import os
import sys

import src.val_tree.adapters.http as http_adp
import src.val_tree.adapters.excell as excell_adp
import src.val_tree.gateways.measurements as measurements_gtw
import src.val_tree.gateways.valuations as valuations_gtw
import src.val_tree.gateways.storage as storage_gtw
import src.val_tree.use_cases.valuation as valuation


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
        valuations_gtw.make(args['reg_sec'], http_adp.make()),
        storage_gtw.make(output_sheet))

    #util.dorun(
    #  map(print_progress
    result = map(valuate_tree, measurements_gtw.iter_trees(input_sheet))
    #      ))

    output_sheet.save()

