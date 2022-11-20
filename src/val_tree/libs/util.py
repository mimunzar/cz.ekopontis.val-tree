#!/usr/bin/env python3
import collections as cl
import functools   as ft
import itertools   as it
import operator    as op
import time


def dorun(iterable):
    cl.deque(iterable, maxlen=0)


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


def mapt(fn, iterable):
    return tuple(map(fn , iterable))


def partition_by(fp, iterable):
    i1, i2 = it.tee(iterable)
    return (filter(fp, i1), filter(complement(fp), i2))


def pluck(iterable, d):
    return op.itemgetter(*iterable)(d)


def pick(iterable, d):
    def do(acc, k):
        acc[k] = d[k]
        return acc
    return ft.reduce(do, iterable, {})


def identity(x):
    return x


def constantly(x):
    return lambda *_: x


def complement(fn):
    return lambda *args: not fn(*args)


def compose(*fn):
    def compose2(fn, other):
        return lambda *args: fn(other(*args))
    return ft.reduce(compose2, fn)


def any_fn(*fn):
    def any_fn2(fn, other):
        return lambda *args: fn(*args) or other(*args)
    return ft.reduce(any_fn2, fn)


def throttle(fn, subsec, fn_sleep=time.sleep):
    start = 0
    def throttled_fn(*args, fn_time=time.time):
        nonlocal start
        elaps = fn_time() - start
        start = start + max(elaps, subsec)
        if elaps < subsec:
            fn_sleep(subsec - elaps)
        return fn(*args)
    return throttled_fn


def make_validator(s, fn):
    to_str = lambda args: ', '.join(map(str, args))
    return lambda *args: (bool(fn(*args)), f'{s} ({to_str(args)})')


def validate_dict(val_d, d):
    return mapt(second, filter(complement(first),
            it.starmap(lambda k, fn: fn(d[k]), val_d.items())))

