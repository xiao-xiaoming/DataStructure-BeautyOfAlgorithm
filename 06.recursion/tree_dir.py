# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

import os
def tree_dir(dir, layer=0):
    listdir = os.listdir(dir)
    for index, file in enumerate(listdir):
        file_path = os.path.join(dir, file)
        print("|  " * (layer - 1), end="")
        if (layer > 0):
            print("`--" if index == len(listdir) - 1 else "|--", end="")
        print(file)
        if (os.path.isdir(file_path)):
            tree_dir(file_path, layer + 1)

tree_dir("..")
