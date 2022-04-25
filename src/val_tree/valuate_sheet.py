#!/usr/bin/env python3

import argparse
import sys

import src.val_tree.gateways.measurements as measurements
import src.val_tree.gateways.valuations   as valuations
import src.val_tree.libs.util as util
import src.val_tree.libs.log  as log


def parse_args(args_it):
    parser = argparse.ArgumentParser()
    parser.add_argument('input-sheet', help='The input Excell sheet with measurements',
            metavar='FILE')
    parser.add_argument('--speed',     help='The number of valuated items per second',
            required=False, metavar="NUM", default=2)
    return vars(parser.parse_args(args_it))


if '__main__' == __name__:
    args = parse_args(sys.argv[1:])

    print(log.fmt_msg('Parsing tree sheet:\n'))
    t_it, err_it = measurements.iter_tree_sheet(args['input-sheet'])
    if (err_it):
        sys.stderr.write(log.fmt_err('Found errors in tree sheet:\n\n'))
        util.consume(map(sys.stderr.write, err_it))
        sys.stderr.write('\nFix errors and re-run the program')
        sys.exit(1)

    # valuations.iter_tree_vals()
