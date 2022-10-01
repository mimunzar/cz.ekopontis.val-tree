#!/usr/bin/env python3

import collections as cl


ProcessedTree = cl.namedtuple('ProcessedTree', [
    'id',
    'value_czk',
])

def make_tree_writer(aFile, should_write_header):
    if should_write_header:
        aFile.write('{}\n'.format(','.join(ProcessedTree._fields)))
    def tree_writer(aValuedTree):
        t = ProcessedTree(id        = aValuedTree.tree.id,
                          value_czk = aValuedTree.value_czk)
        aFile.write('{}\n'.format(','.join(map(str, t))))
        print(f'Written: {t}')
        return t
    return tree_writer

