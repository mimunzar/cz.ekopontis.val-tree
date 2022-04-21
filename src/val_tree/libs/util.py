#!/usr/bin/env python3

import functools as ft
import itertools as it
import operator  as op


def take(n, iterable):
    return it.islice(iterable, n)


def drop(n, iterable):
    return it.islice(iterable, n, None)


def first(iterable):
    return next(iter(iterable))


def nth(n, iterable):
    return first(drop(n, iterable))


def second(iterable):
    return nth(1, iterable)


def pluck(iterable, d):
    return op.itemgetter(*iterable)(d)


def complement(f):
    return lambda *args: not f(*args)


def _compose2(f, g):
    return lambda *args: f(g(*args))


def compose(*f):
    return ft.reduce(_compose2, f)


def _any_fn2(f, g):
    return lambda *args: f(*args) or g(*args)


def any_fn(*f):
    return ft.reduce(_any_fn2, f)


def partition_by(fp, iterable):
    i1, i2 = it.tee(iterable)
    return (filter(fp, i1), filter(complement(fp), i2))


def make_validator(s, f):
    return lambda *args: (bool(f(*args)), s)


def make_checker(Validator):
    def checker(d):
        val_it = it.starmap(lambda k, f: f(d[k]), Validator.items())
        return tuple(map(second, filter(complement(first), val_it)))
    return checker
