#!/usr/bin/env python3

import openpyxl as xl

import src.val_tree.libs.util as util


class ExcellAdapter():
    def __init__(self, fpath):
        self.wb = xl.load_workbook(fpath, data_only=True)

    def first_sheet(self):
        return util.first(self.wb.worksheets)


def make_adapter(fpath):
    return ExcellAdapter(fpath)

