# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

import sys

fs = []
data = []
out = open("out.log", "w", buffering=300 * 1024 * 1024)
for i in range(10):
    fs.append(open("../logs/%s.log" % i, buffering=50 * 1024 * 1024))
    data.append(fs[i].readline().rstrip())

while True:
    min = 0
    for i in range(1, 10):
        if int(data[min]) > int(data[i]):
            min = i
    if data[min] == sys.maxsize: break
    out.write(data[min])
    out.write("\n")
    line = fs[min].readline().rstrip()
    if line:
        data[min] = line
    else:
        data[min] = sys.maxsize

for f in fs:
    f.close()
out.close()