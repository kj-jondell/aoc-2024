import sys, operator
from itertools import groupby, pairwise, starmap

in_d = [[int(n) for n in line.strip().split()] for line in sys.stdin]

def diff_list(diff_list): 
    return (min(diff_list) >= 1 and max(diff_list) <= 3)  or (min(diff_list) >= -3 and max(diff_list) <= -1)

# PART 1
#res = filter(diff_list, [[(x-y) for x, y in zip(l[1:], l[:-1])] for l in in_d])
#print(len(list(res)))

# PART 1 & 2
part1, part2 = 0, 0
res = groupby(sorted([list(starmap(operator.sub, pairwise(l))) for l in in_d], key=diff_list), diff_list) # difference
for k, g in res:
    if k:
        part1 = len(list(g))
    else:
        res = [list(filter(diff_list, [d[1:]] + [d[:i]+[sum(d[i:i+2])]+d[i+2:] for i in range(len(d)-1)] + [d[:-1]])) for d in g]
        part2 = len(list(filter(None, res)))

print(f"part 1: {part1} and part 2: {part1+part2}")
