#!/usr/bin/env python3

import collections as cl
import itertools   as it
import operator    as op
import re

import openpyxl as xl
import requests

import src.val_tree.util as util


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
        "taxon_offset":7,
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

    print(r.json())


def cell_value(c):
    return c.value

INPUT_TRUTHY_VALS = ['a', 'ano', 'y', 'yes']
INPUT_TREE_ROW    = cl.OrderedDict({
    'ID'                                : lambda x: int(x),
    'S/P'                               : lambda x: x,
    'Český název | Latinský název'      : lambda x: x,
    'průměr kmene [cm]'                 : lambda x: tuple(map(float, re.split(';|,', str(x)))),
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
    'rozštípnuté dřevo a trhliny (A/N)' : lambda x: x.lower() in INPUT_TRUTHY_VALS,
    'dutiny (A/N)'                      : lambda x: x.lower() in INPUT_TRUTHY_VALS,
    'hniloba (A/N)'                     : lambda x: x.lower() in INPUT_TRUTHY_VALS,
    'suché větve (A/N)'                 : lambda x: x.lower() in INPUT_TRUTHY_VALS,
    'poškození borky (A/N)'             : lambda x: x.lower() in INPUT_TRUTHY_VALS,
    'výtok mízy (A/N)'                  : lambda x: x.lower() in INPUT_TRUTHY_VALS,
    'zlomené větve (A/N)'               : lambda x: x.lower() in INPUT_TRUTHY_VALS,
    'dutinky (A/N)'                     : lambda x: x.lower() in INPUT_TRUTHY_VALS,
    'plodnice hub (A/N)'                : lambda x: x.lower() in INPUT_TRUTHY_VALS,
    'Památný strom (A/N)'               : lambda x: x.lower() in INPUT_TRUTHY_VALS,
    'Poznámky'                          : lambda x: x,
})

def parse_row(col_it):
    parse_existy = lambda v, k, f: (k, v if None == v else f(v))
    parse        = lambda v, i: parse_existy(v, *i)
    return it.starmap(parse, zip(map(lambda c: c.value, col_it), INPUT_TREE_ROW.items()))


if '__main__' == __name__:
    wb  = xl.load_workbook(filename='.git/input.xlsm', read_only=True, data_only=True)
    ws  = wb.active
    r_i = map(parse_row, util.drop(1, ws.iter_rows()))

