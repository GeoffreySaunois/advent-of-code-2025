import re
from dataclasses import dataclass
import numpy as np

data_path = 'data/test.txt'
# data_path = 'data/in.txt'

with open(data_path) as f:
    path = f.readline()
    f.readline()
    lines = list(map(lambda line_: line_.strip(), f.readlines()))

print(path, lines)

# n, m = len(lines), len(lines[0])
# numbers = {}
# uid = 0
#
# ms = [1 for _ in lines]
# res = 0
# # numbers
# for i, line in enumerate(lines):
#     a, b = map(lambda x: set(map(int, re.split(" +", x))), re.split(" +\| +", re.split(": +", line)[1]))
#     c = len(a.intersection(b))
#     for j in range(c):
#         ms[i + 1 + j] += ms[i]
#     res += ms[i]
#
# print(ms)
#
# print(res)
