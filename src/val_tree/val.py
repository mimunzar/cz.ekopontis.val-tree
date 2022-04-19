#!/usr/bin/env python3

import collections as cl
import itertools   as it
import operator    as op
import re

import openpyxl as xl
import requests

import src.val_tree.util as util
import src.val_tree.tree as tree


def send_request():
    data = {
        "taxon":"borovice černá (Pinus nigra)",
        "diameters":[1080],
        "diameters_on_stumps":[],
        "height":None,
        "stem_height":None,
        "spread":None,
        "vitality":"1",
        "health":"1",
        "removed_crown_volume":None,
        "location_attractiveness":"high",
        "growth_conditions":"unaffected",
        "microhabitats":[],
        "extensive_microhabitats":[],
        "taxon_offset":8,
        "_taxon_cz":"borovice černá",
        "_taxon_lat":"Pinus nigra",
        "memorial_tree":False,
        "deliberately_planted":False
    }

    r = requests.post(
            'https://ocenovanidrevin.nature.cz/hodnota-stromu.php',
            json=data,
            headers={'Content-Type': 'application/json'},
        )

INPUT_TREE_ROW = cl.OrderedDict({
    'ID'                                : lambda x: int(x),
    'S/P'                               : lambda x: x,
    'Český název | Latinský název'      : lambda x: x,
    'průměr kmene [cm]'                 : lambda x: tuple(map(float, re.split(r';|,', str(x)))),
    'obvod kmene [cm]'                  : lambda x: x,
    'výška stromu [m]'                  : lambda x: float(x),
    'výška nasazení koruny [m]'         : lambda x: float(x),
    'průměr koruny [m]'                 : lambda x: float(x),
    'vitalita'                          : lambda x: int(x),
    'zdravotní stav'                    : lambda x: int(x),
    'atraktivita umístění'              : lambda x: int(x),
    'růstové podmínky'                  : lambda x: int(x),
    'biologický význam'                 : lambda x: int(x),
    'odstraněná část koruny [%]'        : lambda x: int(x),
    'rozštípnuté dřevo a trhliny (A/R)' : lambda x: x,
    'dutiny (A/R)'                      : lambda x: x,
    'hniloba (A/R)'                     : lambda x: x,
    'suché větve (A/R)'                 : lambda x: x,
    'poškození borky (A)'               : lambda x: bool(x),
    'výtok mízy (A)'                    : lambda x: bool(x),
    'zlomené větve (A)'                 : lambda x: bool(x),
    'dutinky (A)'                       : lambda x: bool(x),
    'plodnice hub (A)'                  : lambda x: bool(x),
    'Památný strom (A)'                 : lambda x: bool(x),
    'Poznámky'                          : lambda x: x,
})


def parse_row(col_it):
    parse_existy = lambda v, k, f: (k, v if None == v else f(v))
    parse        = lambda v, i: parse_existy(v, *i)
    return dict(it.starmap(parse, zip(map(lambda c: c.value, col_it), INPUT_TREE_ROW.items())))


def from_workbook():
    wb  = xl.load_workbook(filename='.git/input.xlsm', read_only=True, data_only=True)
    ws  = wb.active
    return map(parse_row, util.drop(1, ws.iter_rows()))

if '__main__' == __name__:
    # result = from_workbook()
    result = map(tree.make, from_workbook())

