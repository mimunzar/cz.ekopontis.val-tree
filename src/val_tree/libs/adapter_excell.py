#!/usr/bin/env python3
import openpyxl as xl


class ExcellAdapter:
    def __init__(self, fpath):
        self.fpath = fpath
        self.wb    = xl.load_workbook(fpath, data_only = True)

    def open_sheet(self, title):
        return self.wb[title]


def make(fpath):
    return ExcellAdapter(fpath)

