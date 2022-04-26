#!/usr/bin/env python3

TREE_FIELDS = [
    'id',
]

BUSH_FIELDS = [
    'id',
]

class StorageGateway:
    def __init__(self, excell_adp):
        self.excell_adp = excell_adp
        self.tree_sheet = excell_adp.open_sheet('tree_vals')
        self.bush_sheet = excell_adp.open_sheet('bush_vals')
        self.excell_adp.write_header(self.tree_sheet, TREE_FIELDS)
        self.excell_adp.write_header(self.bush_sheet, BUSH_FIELDS)

    def write_tree_valuation(self, tree, valuation):
        return self.excell_adp.append_row([42])


def make(excell_adp):
    return StorageGateway(excell_adp)

