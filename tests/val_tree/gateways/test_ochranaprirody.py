#!/usr/bin/env python3

import src.val_tree.entities.tree as tree
import src.val_tree.gateways.ochranaprirody as ochranaprirody
import tests.val_tree.constants as constants


def test_from_tree():
    t = tree.from_tree_dat(constants.MEASUREMENT)
    assert ochranaprirody.from_tree(t) == {
        'taxon_offset': 319,
        'taxon': 'jilm horský (Ulmus glabra)',
        '_taxon_cz': 'jilm horský',
        '_taxon_lat': 'Ulmus glabra',
        'diameters': (38,),
        'diameters_on_stumps': [],
        'height': 15.0,
        'stem_height': None,
        'spread': None,
        'vitality': '1',
        'health': '1',
        'removed_crown_volume': None,
        'location_attractiveness': 'less_significant',
        'growth_conditions': 'good',
        'microhabitats': ('i', 'b', 'j', 'h', 'm', 'f', 'a'),
        'extensive_microhabitats': (),
        'memorial_tree': False,
        'deliberately_planted': False,
    }

