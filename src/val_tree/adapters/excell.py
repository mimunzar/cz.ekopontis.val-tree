#!/usr/bin/env python3

import itertools as it
import functools as ft
import os
import openpyxl as xl


def write_cell(ws, r_idx, c_idx, x):
    ws.cell(row=r_idx, column=c_idx, value=x)
    return x


def write_row(ws, r_idx, data_it):
    return tuple(it.starmap(ft.partial(write_cell, ws, r_idx), enumerate(data_it, 1)))


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

    def iter_sheets(self):
        return self.wb.worksheets

    def write_header(self, ws, data_it):
        ws.delete_rows(1)
        ws.insert_rows(1)
        return write_row(ws, 1, data_it)

    def save(self):
        self.wb.save(filename=self.fpath)


def make(fpath):
    return ExcellAdapter(fpath)

