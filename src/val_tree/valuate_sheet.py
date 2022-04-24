#!/usr/bin/env python3

import sys

import src.val_tree.gateways.measurements as measurements
import src.val_tree.gateways.valuations   as valuations
import src.val_tree.libs.util as util
import src.val_tree.libs.log  as log



if '__main__' == __name__:
    if 2 > len(sys.argv):
        sys.stderr.write(log.fmt_err('Missing input file'))
        sys.exit(1)

    print(log.fmt_msg('Parsing tree sheet:\n'))
    t_it, err_it = measurements.iter_tree_sheet(util.second(sys.argv))
    if (err_it):
        sys.stderr.write(log.fmt_err('Found errors in tree sheet:\n\n'))
        util.consume(map(sys.stderr.write, err_it))
        sys.stderr.write('\nFix errors and re-run the program')
        sys.exit(1)

    # valuations.iter_tree_vals()
