#!/usr/bin/env python3

import functools as ft
from time import time


LINE_WIDTH = 80

def fmt_fraction(n, d):
    d_len = len(str(d))
    return f'{n:>{d_len}}/{d}'


def fmt_bar(b_width, total, curr):
    curr = min(curr, total)
    fill = '#'*round(curr/total*b_width)
    return f'[{fill:<{b_width}}] {fmt_fraction(curr, total)}'


def make_prog_bar(b_width, total, l_width=LINE_WIDTH):
    bar = ft.partial(fmt_bar, b_width, total)
    return lambda curr, speed: f'{bar(curr)} ({speed:.02f} rec/s)'.center(l_width)


def make_rec_sec(f_time=time):
    start = f_time()
    def rec_sec(n_rec, f_time=time):
        nonlocal start
        end   = f_time()
        elaps = max(1e-6, end - start)
        start = start + elaps
        return n_rec/elaps
    return rec_sec

