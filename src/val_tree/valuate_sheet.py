#!/usr/bin/env python3

import argparse
import sys

import src.val_tree.adapters.excell as excell
import src.val_tree.gateways.measurements as measurements


def parse_args(args_it):
    parser = argparse.ArgumentParser()
    parser.add_argument('input-sheet', help='The input Excell sheet with measurements',
            metavar='FILE')
    parser.add_argument('--speed',     help='The number of valuated items per second',
            required=False, metavar="NUM", default=2)
    return vars(parser.parse_args(args_it))


if '__main__' == __name__:
    args        = parse_args(sys.argv[1:])
    input_sheet = excell.make_adapter(args['input-sheet'])

    #util.dorun(
    #  map(print_progress
    result = measurements.iter_trees(input_sheet)
    #      ))
