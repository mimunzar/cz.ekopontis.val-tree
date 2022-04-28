#!/usr/bin/env python3

import itertools as it
import functools as ft
import os
import openpyxl as xl
import openpyxl.styles as xl_styles

import src.val_tree.libs.util as util


def fit_row_height(ws, r_idx, d_it):
    ws.row_dimensions[r_idx].height = 6*max(map(len, d_it))


def cell_alignment(params, c):
    c.alignment = xl_styles.Alignment(**params)
    return c


def cell_font(params, c):
    c.font = xl_styles.Font(**params)
    return c


def cell_comma_sep(c):
    c.number_format = '#,##'
    return c


DEFAULT_FONT = {'name': 'FreeMono', 'size': 8}

def cell(ws, r_idx, c_idx, x):
    return cell_font(DEFAULT_FONT, ws.cell(row=r_idx, column=c_idx, value=x))


def iter_cell_row(ws, r_idx, data_it):
    return it.starmap(ft.partial(cell, ws, r_idx), enumerate(data_it, 1))


def create_workbook():
    wb = xl.Workbook()
    wb.remove(wb.active)
    return wb


def load_workbook(fpath):
    return xl.load_workbook(fpath, data_only=True)


def bio_cells(ws, r_idx, c_idx, el_it):
    util.dorun(it.starmap(lambda r, x: cell(ws, r, c_idx, x), enumerate(map(util.first, el_it), r_idx)))
    util.dorun(it.starmap(lambda r, x: cell(ws, r, c_idx + 1, x), enumerate(map(util.second, el_it), r_idx)))


def row_merged_cell(ws, r_idx, c_idx, n, x):
    ws.merge_cells(start_row=r_idx, end_row=r_idx + (n - 1), start_column=c_idx, end_column=c_idx)
    return cell_alignment({'horizontal': 'center', 'vertical': 'center'}, cell(ws, r_idx, c_idx, x))


def col_merged_cell(ws, r_idx, c_idx, n, x):
    ws.merge_cells(start_row=r_idx, end_row=r_idx, start_column=c_idx, end_column=c_idx + (n - 1))
    return cell_alignment({'horizontal': 'center', 'vertical': 'center'}, cell(ws, r_idx, c_idx, x))


TREE_HEADER = {
    'ID'                    : lambda w: cell(w, 1,  1, 'ID'),
    'Název'                 : lambda w: cell(w, 1,  2, 'Název'),
    'Název Lat.'            : lambda w: cell(w, 1,  3, 'Název Lat.'),
    'Průměr Kmene [cm]'     : lambda w: cell(w, 1,  4, 'Průměr Kmene [cm]'),
    'Obvod Kmene [cm]'      : lambda w: cell(w, 1,  5, 'Obvod Kmene [cm]'),
    'Výška Stromu [m]'      : lambda w: cell(w, 1,  6, 'Výška Stromu [m]'),
    'Výška Koruny [m]'      : lambda w: cell(w, 1,  7, 'Výška Koruny [m]'),
    'Průměr Koruny [m]'     : lambda w: cell(w, 1,  8, 'Průměr Koruny [m]'),
    'Odstraněná Koruna [%]' : lambda w: cell(w, 1,  9, 'Odstraněná Koruna [%]'),
    'Vitalita'              : lambda w: cell(w, 1, 10, 'Vitalita'),
    'Zdravotní Stav'        : lambda w: cell(w, 1, 11, 'Zdravotní Stav'),
    'Atraktivita'           : lambda w: cell(w, 1, 12, 'Atraktivita'),
    'Biologické Prvky'      : lambda w: col_merged_cell(w, 1, 13, 2, 'Biologické Prvky'),
    'Hodnota [CZK]'         : lambda w: cell(w, 1, 15, 'Hodnota [CZK]'),
}
TREE_ROW = {
    'ID'                    : lambda w, r, m, t: row_merged_cell(w, r,  1, m, t['ID']),
    'Název'                 : lambda w, r, m, t: row_merged_cell(w, r,  2, m, t['Název']),
    'Název Lat.'            : lambda w, r, m, t: row_merged_cell(w, r,  3, m, t['Název Lat.']),
    'Průměr Kmene [cm]'     : lambda w, r, m, t: row_merged_cell(w, r,  4, m, t['Průměr Kmene [cm]']),
    'Obvod Kmene [cm]'      : lambda w, r, m, t: row_merged_cell(w, r,  5, m, t['Obvod Kmene [cm]']),
    'Výška Stromu [m]'      : lambda w, r, m, t: row_merged_cell(w, r,  6, m, t['Výška Stromu [m]']),
    'Výška Koruny [m]'      : lambda w, r, m, t: row_merged_cell(w, r,  7, m, t['Výška Koruny [m]']),
    'Průměr Koruny [m]'     : lambda w, r, m, t: row_merged_cell(w, r,  8, m, t['Průměr Koruny [m]']),
    'Odstraněná Koruna [%]' : lambda w, r, m, t: row_merged_cell(w, r,  9, m, t['Odstraněná Koruna [%]']),
    'Vitalita'              : lambda w, r, m, t: row_merged_cell(w, r, 10, m, t['Vitalita']),
    'Zdravotní Stav'        : lambda w, r, m, t: row_merged_cell(w, r, 11, m, t['Zdravotní Stav']),
    'Atraktivita'           : lambda w, r, m, t: row_merged_cell(w, r, 12, m, t['Atraktivita']),
    'Biologické Prvky'      : lambda w, r, _, t: bio_cells(w, r, 13, t['Biologické Prvky']),
    'Hodnota [CZK]'         : lambda w, r, m, t: \
            cell_comma_sep(row_merged_cell(w, r, 15, m, t['Hodnota [CZK]'])),
}

class ExcellAdapter:
    def __init__(self, fpath):
        self.fpath = fpath
        if os.path.exists(fpath):
            self.wb = load_workbook(fpath)
        else:
            self.wb = create_workbook()
        self.r_idx  = 2

    def open_sheet(self, title):
        if title in self.wb.get_sheet_names():
            return self.wb[title]
        return self.wb.create_sheet(title)

    def write_header(self, ws, val_it):
        ws.delete_rows(1)
        ws.insert_rows(1)
        val_it = tuple(val_it)
        c_it   = tuple(map(lambda f: f(ws), TREE_HEADER.values()))
        util.dorun(map(ft.partial(cell_font, {
            'name' : 'FreeMono',
            'bold' : True,
            'size' : 8}), c_it))
        util.dorun(map(ft.partial(cell_alignment, {
            'horizontal'   : 'center',
            'vertical'     : 'center',
            'textRotation' : 90}), util.drop(1, c_it)))
        util.dorun(map(ft.partial(cell_alignment, {
            'horizontal' : 'center',
            'vertical'   : 'center'}), util.take(1, c_it)))
        fit_row_height(ws, 1, val_it)

    def append_tree_valuation(self, ws, tree_val):
        n_merged = max(1, len(tree_val['Biologické Prvky']))
        util.dorun(map(lambda f: f(ws, self.r_idx, n_merged, tree_val), TREE_ROW.values()))
        self.r_idx = self.r_idx + n_merged

    def save(self):
        self.wb.save(filename=self.fpath)


def make(fpath):
    return ExcellAdapter(fpath)

