# Time:        48     93     84     66
# Distance:   261   1192   1019   1063

time = 48938466
dist = 261119210191063

lo = 0
hi = time // 2
while lo < hi:
    mi = (lo + hi) // 2
    if mi * (time - mi) > dist:
        hi = mi
    else:
        lo = mi + 1

print(time + 1 - 2 * lo)
