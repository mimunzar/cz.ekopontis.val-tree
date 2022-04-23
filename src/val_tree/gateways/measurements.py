#!/usr/bin/env python3

import functools as ft
import openpyxl as xl

import src.val_tree.entities.measurement as measurement
import src.val_tree.libs.log as log
import src.val_tree.libs.util as util


def col_vals(c_it):
     return map(lambda c: c.value, c_it)


def empty_row(v_it):
    return all(map(lambda c: None == c, v_it))


def make_parser(n_rows):
    speed = log.make_avg_rec_sec()
    bar   = log.make_prog_bar(40, n_rows)
    i     = 0
    print(f'{bar(i, 0)}', end='\r')
    def parser(acc, v_it):
        nonlocal i
        if (not empty_row(v_it)):
            acc.append(measurement.parse_tree(v_it))
        i = i + 1
        print(f'\033[K{bar(i, speed(1))}', end='\n' if n_rows == i else '\r')
        return acc
    return parser


def iter_tree_sheet(fpath):
    ws = xl.load_workbook(filename=fpath, data_only=True).active
    return ft.reduce(make_parser(ws.max_row - 1),
            map(col_vals, util.drop(1, ws.iter_rows())), [])

