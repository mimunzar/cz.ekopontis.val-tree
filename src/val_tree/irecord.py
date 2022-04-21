#!/usr/bin/env python3

import collections as cl
import re

import src.val_tree.libs.util as util


def OPTIONAL():
    return lambda x: None == x


def MATCHES(r):
    return lambda x: r.fullmatch(str(x).strip())


ROW_VALIDATOR = cl.OrderedDict({
    'ID'                                : util.make_validator(
        f'"ID" must be positive int',
        MATCHES(re.compile(r'\d+'))),

    'S/P'                               : util.make_validator(
        f'"S/P" must be one of (S, P)',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'S|P', re.IGNORECASE)))),

    'Český název | Latinský název'      : util.make_validator(
        f'"Český název | Latinský název" must be non-blank',
        MATCHES(re.compile(r'(\S+\s*)+?\|\s*(\S+\s*)+'))),

    'průměr kmene [cm]'                 : util.make_validator(
        f'"průměr kmene [cm]" must contain positive ints',
        MATCHES(re.compile(r'\d+([,;]\d+)*[,;]?'))),

    'obvod kmene [cm]'                  : util.make_validator(
        f'"obvod kmene [cm]" must contain positive ints',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'\d+([,;]\d+)*[,;]?')))),

    'výška stromu [m]'                  : util.make_validator(
        f'"výška stromu [m]" must be positive',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'(\d*\.\d+)|(\d+\.?)')))),

    'výška nasazení koruny [m]'         : util.make_validator(
        f'"výška nasazení koruny [m]" must be positive',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'(\d*\.\d+)|(\d+\.?)')))),

    'průměr koruny [m]'                 : util.make_validator(
        f'"průměr koruny [m]" must be positive',
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

    'odstraněná část koruny [%]'        : util.make_validator(
        f'"odstraněná část koruny [%]" must be positive int',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'100|\d\d|\d')))),

    'rozštípnuté dřevo a trhliny (A/R)' : util.make_validator(
        f'"rozštípnuté dřevo a trhliny (A/R)" must be one of (A, R)',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'A|R', re.IGNORECASE)))),

    'dutiny (A/R)'                      : util.make_validator(
        f'"dutiny (A/R)" must be one of (A, R)',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'A|R', re.IGNORECASE)))),

    'hniloba (A/R)'                     : util.make_validator(
        f'"hniloba (A/R)" must be one of (A, R)',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'A|R', re.IGNORECASE)))),

    'suché větve (A/R)'                 : util.make_validator(
        f'"suché větve (A/R)" must be one of (A, R)',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'A|R', re.IGNORECASE)))),

    'poškození borky (A)'               : util.make_validator(
        f'"poškození borky (A)" must be one of (A)',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'A', re.IGNORECASE)))),

    'výtok mízy (A)'                    : util.make_validator(
        f'"výtok mízy (A)" must be one of (A)',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'A', re.IGNORECASE)))),

    'zlomené větve (A)'                 : util.make_validator(
        f'"zlomené větve (A)" must be one of (A)',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'A', re.IGNORECASE)))),

    'dutinky (A)'                       : util.make_validator(
        f'"dutinky (A)" must be one of (A)',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'A', re.IGNORECASE)))),

    'plodnice hub (A)'                  : util.make_validator(
        f'"plodnice hub (A)" must be one of (A)',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'A', re.IGNORECASE)))),

    'Památný strom (A)'                 : util.make_validator(
        f'"Památný strom (A)" must be one of (A)',
        util.any_fn(OPTIONAL(), MATCHES(re.compile(r'A', re.IGNORECASE)))),
})
ROW_CHECKER = util.make_checker(ROW_VALIDATOR)

def parse(col_it):
    d = dict(zip(ROW_VALIDATOR.keys(), col_it))
    return (d, ROW_CHECKER(d))

