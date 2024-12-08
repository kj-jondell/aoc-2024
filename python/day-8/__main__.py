import sys, re
from itertools import combinations
import numpy as np 
from numpy import array

in_d = {}

for y, line in enumerate(map(str.strip, sys.stdin)):
    width = len(line) - 1
    for x in re.finditer(r'[^\.]', line):
        in_d[x.group(0)] = (in_d[x.group(0)] if x.group(0) in in_d.keys() else []) + [np.array([x.start(), y])]
height = y

## part 1
#antinodes = set()
#for k, v in in_d.items():
#    for f,s in combinations(in_d[k], 2):
#        d = (s-f)
#        if (f-d >= 0).all() and (f-d <= (height, width)).all():
#            antinodes.add(tuple(f-d))
#        if (s+d >= 0).all() and (s+d <= (height, width)).all():
#            antinodes.add(tuple(s+d))

# part 2
antinodes = set()
for v in in_d.values(): 
	for x in v:
		antinodes.add(tuple(x))
for k, v in in_d.items():
    for f,s in combinations(in_d[k], 2):
        d = (s-f)
        while (f-d >= 0).all() and (f-d <= (height, width)).all():
            antinodes.add(tuple(f-d))
            f = f-d
        while (s+d >= 0).all() and (s+d <= (height, width)).all():
            antinodes.add(tuple(s+d))
            s = s+d
print(len(antinodes))

