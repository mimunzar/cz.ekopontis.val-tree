#!/usr/bin/env python3

import collections as cl
import itertools as it

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


TREE_DATA_ROW = cl.OrderedDict({
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

GROWTH_FIELDS = [
    'ID',
]

class StorageGateway:
    def __init__(self, excell_adp):
        self.excell_adp = excell_adp
        self.tree_sheet = excell_adp.open_sheet('oceneni_stromy')
        self.excell_adp.write_header(self.tree_sheet, TREE_DATA_ROW.keys())

    def write_tree_valuation(self, tree, value):
        val_it = it.starmap(lambda k, f: (k, f(tree, value)), TREE_DATA_ROW.items())
        return self.excell_adp.append_tree_valuation(self.tree_sheet, cl.OrderedDict(val_it))


def make(excell_adp):
    return StorageGateway(excell_adp)

