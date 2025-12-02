import re
from dataclasses import dataclass
import numpy as np
import math

# data_path = 'data/test.txt'
data_path = '../data/in.txt'

with open(data_path) as f:
    path = f.readline().strip()
    f.readline()
    lines = list(map(lambda line_: line_.strip(), f.readlines()))

print(path)
g = {}
for line in lines:
    a = line.split(' = ')[0].strip()
    b, c = line.split(' = ')[1].strip()[1:-1].split(', ')
    # print(a, b, c)
    g[(a, 'L')] = b
    g[(a, 'R')] = c

start_pos = []
for x in g.keys():
    if x[0][-1] == 'A' and x[1] == 'L':
        start_pos.append(x[0])
print(start_pos)

start_pos.sort()
res = []
for temp in start_pos:
    print(temp)
    steps = 0
    while temp[-1] != 'Z':
        temp = g[(temp, path[steps % len(path)])]
        steps += 1
    res.append(steps)

print(math.lcm(*res))

##
c = 0
for x in g.keys():
    if x[0][-1] == 'Z':
        c += 1
c
