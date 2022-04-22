#!/usr/bin/env python3

import src.val_tree.libs.log as log


def test_fmt_fraction():
    assert log.fmt_fraction(1, 1)   == '1/1'
    assert log.fmt_fraction(1, 42)  == ' 1/42'
    assert log.fmt_fraction(42, 42) == '42/42'


def test_fmt_bar():
    assert log.fmt_bar(1, 1, 0) == '[ ] 0/1'
    assert log.fmt_bar(1, 1, 1) == '[#] 1/1'
    assert log.fmt_bar(1, 1, 2) == '[#] 1/1'

    assert log.fmt_bar(5, 1, 0)    == '[     ] 0/1'
    assert log.fmt_bar(5, 1, 0.33) == '[##   ] 0.33/1'
    assert log.fmt_bar(5, 1, 1)    == '[#####] 1/1'

    assert log.fmt_bar(10, 5, 0) == '[          ] 0/5'
    assert log.fmt_bar(10, 5, 1) == '[##        ] 1/5'
    assert log.fmt_bar(10, 5, 5) == '[##########] 5/5'


def test_make_prog_bar():
    b = log.make_prog_bar(b_width=1, total=1, l_width=0)
    assert b(0, 0)   == '[ ] 0/1 (0.00 rec/s)'
    assert b(1, 0)   == '[#] 1/1 (0.00 rec/s)'
    assert b(1, 0.5) == '[#] 1/1 (0.50 rec/s)'


def test_make_records_sec():
    rec_sec = log.make_rec_sec(lambda: 0)
    assert rec_sec(1, lambda: 2) == 0.5   # 1 sec diff
    assert rec_sec(5, lambda: 6) == 1.25  # 5 sec diff
    assert rec_sec(5, lambda: 6) == 5e6   # 0 sec diff

