#!/usr/bin/env python3

import pytest

import src.val_tree.entities.tree_dat as tree_dat
import src.val_tree.libs.util as util


def accepted(k, val_it):
    return map(util.first, map(tree_dat.TREE_VALIDATOR[k], val_it))


def rejected(k, val_it):
    return map(util.complement(util.first), map(tree_dat.TREE_VALIDATOR[k], val_it))


def test_ROW_VALIDATOR():
    assert all(accepted('ID', [42, '42']))
    assert all(rejected('ID', [None, -42, '-42', 'foo']))

    assert all(accepted('S/P', [None, 's', 'S', 'p', 'P']))
    assert all(rejected('S/P', [42, 'foo']))

    assert all(accepted('Český název | Latinský název', [
        'foo | bar', 'foo|bar', 'jilm horský | Ulmus glabra']))
    assert all(rejected('Český název | Latinský název', [None, 42, '|foo', 'foo|']))

    assert all(accepted('průměr kmene [cm]', [42, '42', '42,', '42;42;']))
    assert all(rejected('průměr kmene [cm]', [None, 'foo' ',']))

    assert all(accepted('obvod kmene [cm]', [None, 42, '42', '42,', '42;42;']))
    assert all(rejected('obvod kmene [cm]', ['foo' ',']))

    for c in [
            'výška stromu [m]',
            'výška nasazení koruny [m]',
            'průměr koruny [m]'
        ]:
        assert all(accepted(c, [None, 42, '42', '42.', '.42', '4.42']))
        assert all(rejected(c, ['foo' '.']))

    for c in [
            'vitalita',
            'zdravotní stav',
            'atraktivita umístění',
            'růstové podmínky',
            'biologický význam',
        ]:
        assert all(accepted(c, [None, 1, 2, 3, 4, 5, '1', '5']))
        assert all(rejected(c, ['foo', 0, '6']))

    assert all(accepted('odstraněná část koruny [%]', [None, 0, 1, 10, 11, 100, '100']))
    assert all(rejected('odstraněná část koruny [%]', ['foo', 4.2]))

    for c in [
            'rozštípnuté dřevo a trhliny (A/R)',
            'dutiny (A/R)',
            'hniloba (A/R)',
            'suché větve (A/R)',
        ]:
        assert all(accepted(c, [None, 'a', 'A', 'r', 'R']))
        assert all(rejected(c, [42, 'foo']))

    for c in [
            'poškození borky (A)',
            'výtok mízy (A)',
            'zlomené větve (A)',
            'dutinky (A)',
            'plodnice hub (A)',
            'Památný strom (A)',
        ]:
        assert all(accepted(c, [None, 'a', 'A']))
        assert all(rejected(c, [42, 'foo']))


def test_from_data_row():
    row = [ 1, 'S', 'jilm horský | Ulmus glabra', '38', None, 15, None, None, 1, 1, 3, 2, 3, None, 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', None, None, None, None]
    with pytest.raises(ValueError):
        tree_dat.from_data_row(['foo', *row[1:]])
    assert tree_dat.from_data_row(row) == {
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

