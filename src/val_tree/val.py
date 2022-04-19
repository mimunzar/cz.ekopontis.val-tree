#!/usr/bin/env python3

import requests

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


