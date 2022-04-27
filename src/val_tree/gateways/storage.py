#!/usr/bin/env python3

import itertools as it

import src.val_tree.libs.util as util


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
    'Hodnota [CZK]',
]

GROWTH_FIELDS = [
    'ID',
]

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

def bio_elements(microhabitats, extensive_microhabitats):
    habitat_abbr = lambda h: HABITAT_ABBR[h]
    return dict(it.chain(
            zip(map(habitat_abbr, microhabitats), it.repeat('A')),
            zip(map(habitat_abbr, extensive_microhabitats), it.repeat('R')),
        ))


def tree_val_row(tree, valuation):
    hab, ehab = util.pluck(['microhabitats', 'extensive_microhabitats'], tree)
    return {**tree, **valuation, **{
            'diameters_cm' : ';'.join(map(str, tree['diameters_cm'])),
            'radiuses_cm'  : ';'.join(map(str, tree['radiuses_cm'] or [])),
            'bio_elements' : bio_elements(hab, ehab)
        },
    }


class StorageGateway:
    def __init__(self, excell_adp):
        self.excell_adp = excell_adp
        self.tree_sheet = excell_adp.open_sheet('oceneni_stromy')
        self.excell_adp.write_header(self.tree_sheet, TREE_FIELDS)

    def write_tree_valuation(self, tree, valuation):
        return self.excell_adp.append_row(self.tree_sheet, tree_val_row(tree, valuation))


def make(excell_adp):
    return StorageGateway(excell_adp)

