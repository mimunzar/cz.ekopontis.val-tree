#!/usr/bin/env python3

import pytest

import src.val_tree.entities.tree as tree


def test_iter_names():
    assert list(tree.iter_names('foo|bar'))     == ['foo', 'bar']
    assert list(tree.iter_names('foo | bar'))   == ['foo', 'bar']
    assert list(tree.iter_names(' foo | bar ')) == ['foo', 'bar']


def test_iter_trunk_diameter():
    assert list(tree.iter_trunk_diameter(42))       == [42]
    assert list(tree.iter_trunk_diameter('42'))     == [42]
    assert list(tree.iter_trunk_diameter('42;43'))  == [42, 43]
    assert list(tree.iter_trunk_diameter('42;43;')) == [42, 43]
    assert list(tree.iter_trunk_diameter('42,43,')) == [42, 43]


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
    assert tree.from_measurement(m) == {
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
        'memorial_tree': None,
        'deliberately_planted': False,
    }

