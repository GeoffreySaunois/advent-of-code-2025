import re
from dataclasses import dataclass
import numpy as np
import math

# data_path = 'data/a'
data_path = '../data/b'

with open(data_path) as f:
    lines = list(map(lambda line_: list(map(int, line_.strip().split())), f.readlines()))

print(lines)

res = 0
for line in lines:
    temp = 0
    one = 1
    while any(line):
        temp += line[0] * one
        one *= -1
        line = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    res += temp
    print(temp)

print(res)
