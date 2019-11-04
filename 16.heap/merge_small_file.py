# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

import os
from Heap import Heap

fs = []
min_heap = Heap(type="min", sort_key=lambda x: int(x[0]))
out = open("out.log", "w")
for i, filename in enumerate(os.listdir("../logs")):
    fo = open(os.path.join("../logs", filename))
    fs.append(fo)
    min_heap.insert((fo.readline().rstrip(), i))

while True:
    data, i = min_heap.get_top()
    out.write(data)
    out.write("\n")
    line = fs[i].readline().rstrip()
    if line:
        min_heap.update_top((line, i))
    else:
        min_heap.remove_top()
        fs[i].close()
        if min_heap.index == -1: break

out.close()
