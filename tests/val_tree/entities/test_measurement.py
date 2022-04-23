#!/usr/bin/env python3

import src.val_tree.entities.measurement as measurement
import src.val_tree.libs.util as util


def accepted(k, val_it):
    return map(util.first, map(measurement.TREE_VALIDATOR[k], val_it))


def rejected(k, val_it):
    return map(util.complement(util.first), map(measurement.TREE_VALIDATOR[k], val_it))


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

