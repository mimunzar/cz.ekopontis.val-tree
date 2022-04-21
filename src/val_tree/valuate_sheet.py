#!/usr/bin/env python3

import openpyxl as xl
import requests

import src.val_tree.irecord as irecord
import src.val_tree.libs.util as util
import src.val_tree.libs.log as log


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

def make_parser(row_it):
    row_it = tuple(row_it)
    bar    = log.make_prog_bar(40, len(row_it))
    i      = 0
    print(f'{bar(i)}', end='\r')
    def parser(c_it):
        nonlocal i
        r = irecord.parse(c_it)
        i = i + 1
        print(f'\033[K{bar(i)}', end='\n' if len(row_it) == i else '\r')
        return r
    return parser


if '__main__' == __name__:
    wb = xl.load_workbook(filename='.git/input.xlsm', read_only=True, data_only=True)
    non_empty = lambda c_it: any(map(lambda c: c, c_it))
    row_vals  = lambda c_it: tuple(map(lambda c: c.value, c_it))
    row_it    = tuple(filter(non_empty, map(row_vals, util.drop(1, wb.active.iter_rows()))))

    print(log.fmt_msg('Parsing Excell Sheet:\n'))
    result    = tuple(filter(util.second, map(make_parser(row_it), row_it)))

