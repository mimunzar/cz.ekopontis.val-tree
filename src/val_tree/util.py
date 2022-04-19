#!/usr/bin/env python3

import itertools as it


def drop(n, iterable):
    return it.islice(iterable, n, None)

