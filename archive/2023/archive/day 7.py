import re
from dataclasses import dataclass
import numpy as np
import math
from collections import Counter

# data_path = 'data/test.txt'
data_path = '../data/in.txt'

with open(data_path) as f:
    lines = list(map(lambda line_: line_.strip(), f.readlines()))

order = 'AKQT987654321J'[::-1]
order = {x: i for i, x in enumerate(order)}
print(order)

by_cat = {}
line: str
for line in lines:
    a, b = line.split(' ')
    a: str
    print(a)
    j_count = a.count('J')
    aa = a.replace('J', '')
    cat = list(Counter(aa).values())
    cat.sort()

    # best replace
    if cat:
        # m = max(cat)
        # best_replace = 'z'
        # replace_score = -1
        # for letter, count in Counter(aa).items():
        #     if count == m:
        #         if order[letter] > replace_score:
        #             replace_score = order[letter]
        #             best_replace = letter
        # a = a.replace('J', best_replace)
        cat[-1] += j_count
    else:
        cat = [5]
        # a = 'AAAAA'
    cat = tuple(cat)
    print(line, cat, a)
    if cat in by_cat:
        by_cat[cat].append((a, b))
    else:
        by_cat[cat] = [(a, b)]

print(by_cat)

cats = [
    (1, 1, 1, 1, 1),
    (1, 1, 1, 2),
    (1, 2, 2),
    (1, 1, 3),
    (2, 3),
    (1, 4),
    (5,)
]

res = 0
counter = 1
for cat in cats:
    if cat in by_cat:
        equals = by_cat[cat]
        equals.sort(key=lambda x: list(map(lambda c: order[c], list(x[0]))))
        print(equals, 'meh')
        for a, b in equals:
            res += counter * int(b)
            counter += 1
print(res)
