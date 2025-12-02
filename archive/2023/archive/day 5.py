import re
from dataclasses import dataclass
import numpy as np
import math

# data_path = 'data/test.txt'
data_path = '../data/in.txt'

with open(data_path) as f:
	seeds = f.readline().strip().split(': ')[1].split()
	f.readline()
	f.readline()
	lines = list(map(lambda line_: line_.strip(), f.readlines()))

# print(seeds)
# print(lines)

ind = 0
maps = []
while ind < len(lines):

	maps.append([])
	line = lines[ind]
	while line != '' and ind < len(lines):
		b, a, r = line.strip().split()
		maps[-1].append((a, b, r))
		ind += 1
		if ind < len(lines):
			line = lines[ind]
	ind += 2

mvp = 100000000000000
# print('maps', maps)
maps = list(map(lambda x: list(map(lambda y: list(map(int, y)), x)), maps))
for x in maps:
	x.sort()
	x.append([mvp, mvp, 1])
# print('maps', maps)

seeds = list(map(int, seeds))
# print(seeds)

sss = []
for i in range(len(seeds) // 2):
	sss.append((seeds[2 * i], seeds[2 * i + 1]))

seeds = sss
print(seeds)
res = 100000000000000
for seed_range in seeds:
	to_see = [seed_range]
	for ind_map, m in enumerate(maps):
		print(f'---map {ind_map}, to_see:', to_see)
		new_seed_range = []
		ind = 0
		begin, length = to_see[ind]
		for i, (a, b, r) in enumerate(m[:-1]):
			aa, bb, rr = m[i + 1]
			while begin < aa:
				print((begin, length), (a, b, r), (aa, bb, rr))
				print('ie', (a, a + r - 1, b), (aa, aa + rr - 1, bb))
				if a <= begin < a + r:
					print('meh')
					if a <= begin + length <= a + r:
						new_seed_range.append((b + begin - a, length))
						# go next val
						print('here', new_seed_range)
						ind += 1
						if ind == len(to_see):
							break
						else:
							begin, length = to_see[ind]
					elif begin + length <= aa:
						new_seed_range.append((b + begin - a, a + r - begin))
						new_seed_range.append((a + r, begin + length - (a + r)))
						# go next val
						print('here2', new_seed_range)
						ind += 1
						if ind == len(to_see):
							break
						else:
							begin, length = to_see[ind]
					else:
						new_seed_range.append((b + begin - a, a + r - begin))
						if aa > a + r:
							new_seed_range.append((a + r, aa - a - r))
						# update val
						print('here3', new_seed_range)
						begin, length = aa, begin + length - aa
				else:
					if begin + length <= aa:
						new_seed_range.append((begin, length))
						# go next val
						print('here4', new_seed_range)
						ind += 1
						if ind == len(to_see):
							break
						else:
							begin, length = to_see[ind]
					else:
						new_seed_range.append((begin, aa - begin))
						# update val
						print('here5', new_seed_range)
						begin, length = aa, begin + length - aa
			if ind == len(to_see):
				break
		print('recap', m, to_see, ind, new_seed_range)
		new_seed_range.sort()
		to_see = new_seed_range
	print('---final s', to_see)
	if to_see[0][0] < res:
		res = to_see[0][0]

print(res)
