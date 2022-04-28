#!/usr/bin/env python3

import src.val_tree.gateways.storage as storage


def test_bio_elements():
    assert storage.iter_bio_elements(['dutiny (A/R)'], []) == (('DUT', 'A'),)
    assert storage.iter_bio_elements([], ['dutiny (A/R)']) == (('DUT', 'R'),)
    assert storage.iter_bio_elements([
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
        ]) == (
            ('TRH', 'A'),
            ('DUT', 'A'),
            ('HNI', 'A'),
            ('SUV', 'A'),
            ('BOR', 'A'),
            ('MIZ', 'A'),
            ('ZLV', 'R'),
            ('DUK', 'R'),
            ('PHU', 'R'),
        )

