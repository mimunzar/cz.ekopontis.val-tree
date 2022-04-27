#!/usr/bin/env python3

import itertools as it
import functools as ft
import os
import openpyxl as xl
import openpyxl.styles as xl_styles

import src.val_tree.libs.util as util


def fit_row_height(ws, r_idx, d_it):
    ws.row_dimensions[r_idx].height = 6*max(map(len, d_it))


def set_cell_alignment(params, c):
    c.alignment = xl_styles.Alignment(**params)
    return c


def set_cell_font(params, c):
    c.font = xl_styles.Font(**params)
    return c


def write_cell(ws, r_idx, c_idx, x):
    return set_cell_font({'name': 'FreeMono'}, ws.cell(row=r_idx, column=c_idx, value=x))


def iter_write_row(ws, r_idx, data_it):
    return it.starmap(ft.partial(write_cell, ws, r_idx), enumerate(data_it, 1))


def create_workbook():
    wb = xl.Workbook()
    wb.remove(wb.active)
    return wb


def load_workbook(fpath):
    return xl.load_workbook(fpath, data_only=True)


class ExcellAdapter:
    def __init__(self, fpath):
        self.fpath = fpath
        if os.path.exists(fpath):
            self.wb = load_workbook(fpath)
        else:
            self.wb = create_workbook()

    def open_sheet(self, title):
        if title in self.wb.get_sheet_names():
            return self.wb[title]
        return self.wb.create_sheet(title)

    def write_header(self, ws, data_it):
        ws.delete_rows(1)
        ws.insert_rows(1)
        data_it = tuple(data_it)
        c_it    = tuple(iter_write_row(ws, 1, data_it))
        util.dorun(map(ft.partial(set_cell_font, {
            'name' : 'FreeMono',
            'bold' : True,
            'size' : 8}), c_it))
        util.dorun(map(ft.partial(set_cell_alignment, {
            'horizontal'   : 'center',
            'vertical'     : 'center',
            'textRotation' : 90}), util.drop(1, c_it)))
        util.dorun(map(ft.partial(set_cell_alignment, {
            'horizontal' : 'center',
            'vertical'   : 'center'}), util.take(1, c_it)))
        fit_row_height(ws, 1, data_it)

    def save(self):
        self.wb.save(filename=self.fpath)


def make(fpath):
    return ExcellAdapter(fpath)

