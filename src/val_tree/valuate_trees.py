#!/usr/bin/env python3

import openpyxl as xl
import requests

import src.val_tree.irecord as irecord
import src.val_tree.libs.util as util


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


def from_workbook():
    wb = xl.load_workbook(filename='.git/input.xlsm', read_only=True, data_only=True)
    return map(lambda r: map(lambda c: c.value, r), util.drop(1, wb.active.iter_rows()))


if '__main__' == __name__:
    result = map(irecord.parse, from_workbook())

