#!/usr/bin/env python3

import src.val_tree.libs.util as util


TREE_API = 'https://ocenovanidrevin.nature.cz/hodnota-stromu.php'

class ValuationGateway:
    def __init__(self, reg_sec, http_adp):
        self.post = util.throttle(http_adp.post, 1/reg_sec)

    def valuate_tree(self, tree):
        return self.post(TREE_API, tree)


def make(reg_sec, http_adp):
    return ValuationGateway(reg_sec, http_adp)

