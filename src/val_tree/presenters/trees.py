#!/usr/bin/env python3

import collections as cl
import functools as ft
import itertools as it

import src.val_tree.adapters.excell as excell
import src.val_tree.libs.util as util


HABITAT_ABBR = {
    'rozštípnuté dřevo a trhliny (A/R)' : 'TRH',
    'dutiny (A/R)'                      : 'DUT',
    'hniloba (A/R)'                     : 'HNI',
    'suché větve (A/R)'                 : 'SUV',
    'poškození borky (A)'               : 'BOR',
    'výtok mízy (A)'                    : 'MIZ',
    'zlomené větve (A)'                 : 'ZLV',
    'dutinky (A)'                       : 'DUK',
    'plodnice hub (A)'                  : 'PHU',
}

def iter_bio_elements(microhabitats, extensive_microhabitats):
    habitat_abbr = lambda h: HABITAT_ABBR[h]
    return tuple(it.chain(
            zip(map(habitat_abbr, microhabitats), it.repeat('A')),
            zip(map(habitat_abbr, extensive_microhabitats), it.repeat('R')),
        ))


PRESS_DATA = cl.OrderedDict({
    'ID'                    : lambda t, _: t['id'],
    'Název'                 : lambda t, _: t['name'],
    'Název Lat.'            : lambda t, _: t['name_lat'],
    'Průměr Kmene [cm]'     : lambda t, _: ';'.join(map(str, t['diameters_cm'])),
    'Obvod Kmene [cm]'      : lambda t, _: ';'.join(map(str, t['radiuses_cm'] or [])),
    'Výška Stromu [m]'      : lambda t, _: t['height_m'],
    'Výška Koruny [m]'      : lambda t, _: t['stem_height_m'],
    'Průměr Koruny [m]'     : lambda t, _: t['crown_diameter_m'],
    'Odstraněná Koruna [%]' : lambda t, _: t['removed_crown_volume_perc'],
    'Vitalita'              : lambda t, _: t['vitality'],
    'Zdravotní Stav'        : lambda t, _: t['health'],
    'Atraktivita'           : lambda t, _: t['location_attractiveness'],
    'Biologické Prvky'      : lambda t, _: \
        iter_bio_elements(*util.pluck(['microhabitats', 'extensive_microhabitats'], t)),
    'Hodnota [CZK]'         : lambda _, v: v['value_czk'],
})

def present(tree, value):
    return dict(it.starmap(lambda k, f: (k, f(tree, value)), PRESS_DATA.items()))


HEADER = {
    'ID'                    : lambda w: excell.cell(w, 1,  1, 'ID'),
    'Název'                 : lambda w: excell.cell(w, 1,  2, 'Název'),
    'Název Lat.'            : lambda w: excell.cell(w, 1,  3, 'Název Lat.'),
    'Průměr Kmene [cm]'     : lambda w: excell.cell(w, 1,  4, 'Průměr Kmene [cm]'),
    'Obvod Kmene [cm]'      : lambda w: excell.cell(w, 1,  5, 'Obvod Kmene [cm]'),
    'Výška Stromu [m]'      : lambda w: excell.cell(w, 1,  6, 'Výška Stromu [m]'),
    'Výška Koruny [m]'      : lambda w: excell.cell(w, 1,  7, 'Výška Koruny [m]'),
    'Průměr Koruny [m]'     : lambda w: excell.cell(w, 1,  8, 'Průměr Koruny [m]'),
    'Odstraněná Koruna [%]' : lambda w: excell.cell(w, 1,  9, 'Odstraněná Koruna [%]'),
    'Vitalita'              : lambda w: excell.cell(w, 1, 10, 'Vitalita'),
    'Zdravotní Stav'        : lambda w: excell.cell(w, 1, 11, 'Zdravotní Stav'),
    'Atraktivita'           : lambda w: excell.cell(w, 1, 12, 'Atraktivita'),
    'Biologické Prvky'      : lambda w: excell.col_merged_cell(w, 1, 13, 2, 'Biologické Prvky'),
    'Hodnota [CZK]'         : lambda w: excell.cell(w, 1, 15, 'Hodnota [CZK]'),
}
ROW = {
    'ID'                    : lambda w, r, m, t: excell.row_merged_cell(w, r,  1, m, t['ID']),
    'Název'                 : lambda w, r, m, t: excell.row_merged_cell(w, r,  2, m, t['Název']),
    'Název Lat.'            : lambda w, r, m, t: excell.row_merged_cell(w, r,  3, m, t['Název Lat.']),
    'Průměr Kmene [cm]'     : lambda w, r, m, t: excell.row_merged_cell(w, r,  4, m, t['Průměr Kmene [cm]']),
    'Obvod Kmene [cm]'      : lambda w, r, m, t: excell.row_merged_cell(w, r,  5, m, t['Obvod Kmene [cm]']),
    'Výška Stromu [m]'      : lambda w, r, m, t: excell.row_merged_cell(w, r,  6, m, t['Výška Stromu [m]']),
    'Výška Koruny [m]'      : lambda w, r, m, t: excell.row_merged_cell(w, r,  7, m, t['Výška Koruny [m]']),
    'Průměr Koruny [m]'     : lambda w, r, m, t: excell.row_merged_cell(w, r,  8, m, t['Průměr Koruny [m]']),
    'Odstraněná Koruna [%]' : lambda w, r, m, t: excell.row_merged_cell(w, r,  9, m, t['Odstraněná Koruna [%]']),
    'Vitalita'              : lambda w, r, m, t: excell.row_merged_cell(w, r, 10, m, t['Vitalita']),
    'Zdravotní Stav'        : lambda w, r, m, t: excell.row_merged_cell(w, r, 11, m, t['Zdravotní Stav']),
    'Atraktivita'           : lambda w, r, m, t: excell.row_merged_cell(w, r, 12, m, t['Atraktivita']),
    'Biologické Prvky'      : lambda w, r, _, t: excell.bio_cells(w, r, 13, t['Biologické Prvky']),
    'Hodnota [CZK]'         : lambda w, r, m, t: \
            excell.cell_comma_sep(excell.row_merged_cell(w, r, 15, m, t['Hodnota [CZK]'])),
}

def write_header(ws, label_it):
    ws.delete_rows(1)
    ws.insert_rows(1)
    label_it = tuple(label_it)
    cell_it  = tuple(map(lambda f: f(ws), HEADER.values()))
    util.dorun(map(ft.partial(excell.cell_font, {
        'name' : 'FreeMono',
        'bold' : True,
        'size' : 8}), cell_it))
    util.dorun(map(ft.partial(excell.cell_alignment, {
        'horizontal'   : 'center',
        'vertical'     : 'center',
        'textRotation' : 90}), util.drop(1, cell_it)))
    util.dorun(map(ft.partial(excell.cell_alignment, {
        'horizontal' : 'center',
        'vertical'   : 'center'}), util.take(1, cell_it)))
    excell.fit_row_height(ws, 1, label_it)


def append_valuation(ws, r_idx, tree_val):
    n_merged = max(1, len(tree_val['Biologické Prvky']))
    util.dorun(map(lambda f: f(ws, r_idx, n_merged, tree_val), ROW.values()))
    return r_idx + n_merged


class TreePresenter:
    def __init__(self, excell_adp):
        self.r_idx      = 2
        self.excell_adp = excell_adp
        self.tree_sheet = excell_adp.open_sheet('oceneni_stromy')
        write_header(self.tree_sheet, ROW.keys())

    def write_valuation(self, tree, value):
        self.r_idx = append_valuation(self.tree_sheet, self.r_idx, present(tree, value))
        return (tree, value)


def make(excell_adp):
    return TreePresenter(excell_adp)

