#!/usr/bin/env python3

import pytest

import src.val_tree.entities.tree as tree


def test_iter_names():
    assert list(tree.iter_names('foo|bar'))     == ['foo', 'bar']
    assert list(tree.iter_names('foo | bar'))   == ['foo', 'bar']
    assert list(tree.iter_names(' foo | bar ')) == ['foo', 'bar']


def test_iter_int_csv():
    assert list(tree.iter_int_csv(42))       == [42]
    assert list(tree.iter_int_csv('42'))     == [42]
    assert list(tree.iter_int_csv('42;43'))  == [42, 43]
    assert list(tree.iter_int_csv('42;43;')) == [42, 43]
    assert list(tree.iter_int_csv('42,43,')) == [42, 43]


def test_iter_habitats():
    with pytest.raises(KeyError):
        tree.iter_habitats(['foo'], ['a'], {})
    assert list(tree.iter_habitats(['foo'], ['a'], {'foo': None})) == []
    assert list(tree.iter_habitats(['foo'], ['a'], {'foo': 'a'}))  == ['foo']
    assert list(tree.iter_habitats(['foo', 'bar'],
        ['a', 'A'], {'foo': 'a', 'bar': 'A'})) == ['foo', 'bar']


def test_from_measurement():
    m = {
        'ID': 1,
        'S/P': 'S',
        'Český název | Latinský název': 'jilm horský | Ulmus glabra',
        'průměr kmene [cm]': '38',
        'obvod kmene [cm]': None,
        'výška stromu [m]': 15,
        'výška nasazení koruny [m]': None,
        'průměr koruny [m]': None,
        'vitalita': 1,
        'zdravotní stav': 1,
        'atraktivita umístění': 3,
        'růstové podmínky': 2,
        'biologický význam': 3,
        'odstraněná část koruny [%]': None,
        'rozštípnuté dřevo a trhliny (A/R)': 'A',
        'dutiny (A/R)': 'A',
        'hniloba (A/R)': 'A',
        'suché větve (A/R)': 'A',
        'poškození borky (A)': 'A',
        'výtok mízy (A)': 'A',
        'zlomené větve (A)': 'A',
        'dutinky (A)': 'A',
        'plodnice hub (A)': None,
        'Památný strom (A)': None
    }
    assert tree.from_tree_dat(m) == {
        'id': 1,
        'name': 'jilm horský',
        'name_lat': 'Ulmus glabra',
        'diameters_cm': (38,),
        'radiuses_cm': None,
        'height_m': 15.0,
        'stem_height_m': None,
        'vitality': 1,
        'health': 1,
        'crown_diameter_m': None,
        'removed_crown_volume_perc': None,
        'location_attractiveness': 3,
        'growth_conditions': 2,
        'microhabitats': ('rozštípnuté dřevo a trhliny (A/R)',
            'dutiny (A/R)',
            'suché větve (A/R)',
            'poškození borky (A)',
            'výtok mízy (A)',
            'zlomené větve (A)',
            'dutinky (A)'),
        'extensive_microhabitats': (),
        'memorial_tree': False
    }

