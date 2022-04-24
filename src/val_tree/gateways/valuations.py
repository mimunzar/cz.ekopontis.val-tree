#!/usr/bin/env python3

import requests

import src.val_tree.libs.util as util


TREE_API_URL = 'https://ocenovanidrevin.nature.cz/hodnota-stromu.php'

def valuate_tree(tree):
    return requests.post(TREE_API_URL,
        headers={'Content-Type': 'application/json'},
        json=tree,
    )

def iter_tree_vals(tree_it):
    return map(util.throttle(valuate_tree, 0.5), tree_it)


