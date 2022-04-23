#!/usr/bin/env python3

import sys
import requests

import src.val_tree.gateways.measurements as measurements
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

if '__main__' == __name__:
    if 2 > len(sys.argv):
        print(log.fmt_err('Missing input file'), file=sys.stderr)
        sys.exit(1)


    print(log.fmt_msg('Parsing Tree Sheet:\n'))
    mt_it = measurements.iter_tree_sheet(util.second(sys.argv))
    # vt_it = valuations.iter_tree_vals(map(tree.from_measurement, m_it))
    sys.exit(0)

