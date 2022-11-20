#!/usr/bin/env python3

import collections as cl
import math        as ma
import re

import src.val_tree.libs.util as util


def OPTIONAL(): return lambda x: None == x
def MATCHES(r): return lambda x: r.fullmatch(str(x).strip())
def ANY()     : return lambda _: True


TREE_ROW_VALIDATOR = cl.OrderedDict({
    'id'                                : util.make_validator(
        f'"ID" must be positive int',
        MATCHES(re.compile(r'S\d+'))),

    'český název'                       : util.make_validator(
        f'"Český název" must be non-blank',
        MATCHES(re.compile(r'(\S+\s*)+'))),

    'latinský název'                    : util.make_validator(
        f'"Latinský název" must be non-blank',
        MATCHES(re.compile(r'(\S+\s*)+'))),

    'průměr kmenů [cm]'                 : util.make_validator(
        f'"průměr kmenů [cm]" must contain positive ints',
        MATCHES(re.compile(r'(\d*\.\d+)|(\d+\.?)'))),

    'obvod kmenů [cm]'                  : util.make_validator(
        f'"obvod kmenů [cm]" must contain positive ints',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'(\d*\.\d+)|(\d+\.?)')))),

    'výška stromu [m]'                  : util.make_validator(
        f'"výška stromu [m]" must be positive number',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'(\d*\.\d+)|(\d+\.?)')))),

    'vitalita'                          : util.make_validator(
        f'"vitalita" must be in range of <1, 5>',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'[1-5]')))),

    'zdravotní stav'                    : util.make_validator(
        f'"zdravotní stav" must be in range of <1, 5>',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'[1-5]')))),

    'atraktivita umístění'              : util.make_validator(
        f'"atraktivita umístění" must be in range of <1, 5>',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'[1-5]')))),

    'růstové podmínky'                  : util.make_validator(
        f'"růstové podmínky" must be in range of <1, 5>',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'[1-5]')))),

    'biologický význam'                 : util.make_validator(
        f'"biologický význam" must be in range of <1, 5>',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'[1-5]')))),

    'poznámka'                          : util.make_validator(
        f'"poznámka" can be anything',
        ANY()),

    'nadlimitní Ano/Ne'                 : util.make_validator(
        f'"nadlimitní Ano/Ne" must be Ano or Ne',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'A|N', re.IGNORECASE)))),

    'povolení kácení Ano/Ne'            : util.make_validator(
        f'"povolení kácení Ano/Ne" must be Ano or Ne',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'A|N', re.IGNORECASE)))),
})

RADIUS_RE = re.compile(r'(?:\s*\d+;)+\s*\d+')

def read_tree_radiuses(s):
    if m := RADIUS_RE.search(s):
        return util.mapt(int, m.group(0).split(';'))
    return tuple()


Tree = cl.namedtuple('Tree', [
    'id',
    'name_cz',
    'name_lat',
    'diameters_cm',
    'height_m',
    'vitality',
    'health',
    'location_attractiveness',
    'growth_conditions',
])
def make_tree_parser():
    keys        = TREE_ROW_VALIDATOR.keys()
    parser      = util.make_checker(TREE_ROW_VALIDATOR)
    rad_to_diam = lambda x: round(float(x)/ma.pi)
    def tree_trunk_diameters(aTreeRow):
        if note := aTreeRow['poznámka']:
            if rads := read_tree_radiuses(note):
                return util.mapt(rad_to_diam, rads)
        return (int(aTreeRow['průměr kmenů [cm]']),)
    def tree_parser(vals):
        row = dict(zip(keys, vals))
        if err := parser(row):
            raise ValueError(f'Failed to parse tree ({", ".join(err)})')
        return Tree(
                id                      = row['id'],
                name_cz                 = row['český název'],
                name_lat                = row['latinský název'],
                diameters_cm            = tree_trunk_diameters(row),
                height_m                = int(row['výška stromu [m]']),
                vitality                = int(row['vitalita']),
                health                  = int(row['zdravotní stav']),
                location_attractiveness = int(row['atraktivita umístění']),
                growth_conditions       = int(row['růstové podmínky']))
    return tree_parser

