#!/usr/bin/env python3

TREE_FIELDS = [
    'ID',
    'Název',
    'Název Lat.',
    'Průměr Kmene [cm]',
    'Obvod Kmene [cm]',
    'Výška Stromu [m]',
    'Výška Koruny [m]',
    'Průměr Koruny [m]',
    'Odstraněná Koruna [%]',
    'Vitalita',
    'Zdravotní Stav',
    'Atraktivita',
    'Biologické Prvky',
]

GROWTH_FIELDS = [
    'ID',
]

def tree_val_row(tree, valuation):
    return []


class StorageGateway:
    def __init__(self, excell_adp):
        self.excell_adp = excell_adp
        self.tree_sheet = excell_adp.open_sheet('oceneni_stromy')
        self.excell_adp.write_header(self.tree_sheet, TREE_FIELDS)

    def write_tree_valuation(self, tree, valuation):
        return self.excell_adp.append_row(self.tree_sheet, tree_val_row(tree, valuation))


def make(excell_adp):
    return StorageGateway(excell_adp)

