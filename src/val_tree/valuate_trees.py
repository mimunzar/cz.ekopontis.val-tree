#!/usr/bin/env python3

import argparse
import sys
import os

import src.val_tree.gateways.reader     as reader
import src.val_tree.gateways.valuator   as valuator
import src.val_tree.gateways.writer     as writer
import src.val_tree.libs.adapter_excell as adapter_excell
import src.val_tree.libs.util           as util


def parse_args(args_it):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-fpath',
        help    = 'The Excell WorkBook with measurements',
        metavar = 'FILE')
    parser.add_argument('--trees-per-sec',
        help    = 'The number of valuated items per second',
        metavar = 'NUM',
        type    = int)
    return vars(parser.parse_args(args_it))


def count_trees_written(output_fpath):
    result = 0
    if os.path.exists(output_fpath):
        with open(output_fpath, 'r') as f:
            result = sum(1 for _ in f)
            print(f'Found file with {result} lines written')
    return result


def valuate_new_trees(output_fpath, input_fpath, trees_per_sec, **_):
    iworkbook     = adapter_excell.make(input_fpath)
    tree_sheet    = iworkbook.open_sheet('Stromy')
    trees_written = count_trees_written(output_fpath)
    with open(output_fpath, 'a') as f:
        should_write_header = not trees_written
        skip_n_lines        = max(1, trees_written)
        util.dorun(map(util.compose(
            writer  .make_tree_writer(f, should_write_header),
            valuator.make_tree_valuator(trees_per_sec),
            reader  .make_tree_parser(),
        ), util.drop(skip_n_lines, tree_sheet.iter_rows(values_only = True))))


if '__main__' == __name__:
    valuate_new_trees('output.csv', **parse_args(sys.argv[1:]))

