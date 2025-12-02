import re
from dataclasses import dataclass
import numpy as np
import math

# data_path = 'data/a'
data_path = '../data/b'

with open(data_path) as f:
    lines = list(map(lambda line_: list(map(int, line_.strip().split())), f.readlines()))

print(lines)
