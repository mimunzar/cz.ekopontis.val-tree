#!/usr/bin/env python3

import functools as ft

import src.val_tree.libs.util as util


def optional_apply(f, x):
    return x if None == x else f(x)


def iter_int_csv(x):
    return tuple(map(int, filter(util.identity, str(x).replace(',', ';').split(';'))))


HABITAT_KEYS = [
    'rozštípnuté dřevo a trhliny (A/R)',
    'dutiny (A/R)',
    'suché větve (A/R)',
    'poškození borky (A)',
    'výtok mízy (A)',
    'zlomené větve (A)',
    'dutinky (A)',
    'plodnice hub (A)',
]

def iter_habitats(keys_it, tags_it, m):
    h_it = zip(keys_it, util.pluck(keys_it, m) or [])
    return map(util.first, filter(lambda x: util.second(x) in tags_it, h_it))


iter_microhabitats     = ft.partial(iter_habitats, HABITAT_KEYS, ['a', 'A'])
iter_ext_microhabitats = ft.partial(iter_habitats, HABITAT_KEYS, ['r', 'R'])

def iter_names(names):
    return map(lambda s: s.strip(), names.split(r'|'))


def from_tree_dat(m):
    cz, lat = iter_names(m['Český název | Latinský název'])
    return {
        'id'                       : m['ID'],
        'name'                     : cz,
        'name_lat'                 : lat,
        'diameters_cm'             : iter_int_csv(m['průměr kmene [cm]']),
        'radiuses_cm'              : optional_apply(iter_int_csv, m['obvod kmene [cm]']),
        'height_m'                 : optional_apply(float, m['výška stromu [m]']),
        'stem_height_m'            : optional_apply(float, m['výška nasazení koruny [m]']),
        'vitality'                 : optional_apply(int, m['vitalita']),
        'health'                   : optional_apply(int, m['zdravotní stav']),
        'crown_diameter_m'         : optional_apply(float, m['průměr koruny [m]']),
        'removed_crown_volume_perc': optional_apply(int, m['odstraněná část koruny [%]']),
        'location_attractiveness'  : optional_apply(int, m['atraktivita umístění']),
        'growth_conditions'        : optional_apply(int, m['růstové podmínky']),
        'microhabitats'            : tuple(iter_microhabitats(m)),
        'extensive_microhabitats'  : tuple(iter_ext_microhabitats(m)),
        'memorial_tree'            : bool(m['Památný strom (A)']),
    }

