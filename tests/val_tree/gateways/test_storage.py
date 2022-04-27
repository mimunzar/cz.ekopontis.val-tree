#!/usr/bin/env python3

import src.val_tree.gateways.storage as storage
import src.val_tree.entities.tree as tree
import tests.val_tree.constants as constants


def test_bio_elements():
    assert storage.bio_elements(['dutiny (A/R)'], []) == {'DUT': 'A'}
    assert storage.bio_elements([], ['dutiny (A/R)']) == {'DUT': 'R'}
    assert storage.bio_elements([
            'rozštípnuté dřevo a trhliny (A/R)',
            'dutiny (A/R)',
            'hniloba (A/R)',
            'suché větve (A/R)',
            'poškození borky (A)',
            'výtok mízy (A)',
        ], [
            'zlomené větve (A)',
            'dutinky (A)',
            'plodnice hub (A)',
        ]) == {
            'TRH': 'A',
            'DUT': 'A',
            'HNI': 'A',
            'SUV': 'A',
            'BOR': 'A',
            'MIZ': 'A',
            'ZLV': 'R',
            'DUK': 'R',
            'PHU': 'R',
        }


def test_tree_val_row():
    t = tree.from_measurement(constants.MEASUREMENT)
    v = {'value_in_czk': 42}
    assert storage.tree_val_row(t, v) == {
        'id': 1,
        'name': 'jilm horský',
        'name_lat': 'Ulmus glabra',
        'diameters_cm': '38',
        'radiuses_cm': '',
        'height_m': 15.0,
        'stem_height_m': None,
        'vitality': 1,
        'health': 1,
        'crown_diameter_m': None,
        'removed_crown_volume_perc': None,
        'location_attractiveness': 3,
        'growth_conditions': 2,
        'microhabitats': (
            'rozštípnuté dřevo a trhliny (A/R)',
            'dutiny (A/R)',
            'suché větve (A/R)',
            'poškození borky (A)',
            'výtok mízy (A)',
            'zlomené větve (A)',
            'dutinky (A)'
        ),
        'extensive_microhabitats': (),
        'memorial_tree': False,
        'value_in_czk': 42,
        'bio_elements': {
            'TRH': 'A',
            'DUT': 'A',
            'SUV': 'A',
            'BOR': 'A',
            'MIZ': 'A',
            'ZLV': 'A',
            'DUK': 'A'
            }
        }

