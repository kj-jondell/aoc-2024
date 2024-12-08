import sys
import os
from itertools import pairwise

level = int(os.environ.get("LEVEL", 1))

def get_cond():
    while (line := next(sys.stdin).strip()):
        yield line.split("|")

conditions=[(int(x), int(y)) for x, y in get_cond()]

q=[list(map(int, line.split(","))) for line in sys.stdin]
s=[list(map(lambda b: b in conditions, pairwise(i))) for i in q]
 
match level:

    case 1:
        print(sum([j[len(j)//2] for j, k in zip(q,s) if False not in k]))

    case 2:
        s = [(j,[o for o,b in enumerate(k) if not b]) for j, k in zip(q,s) if False in k]

        def order(l_nums, indices):
            if indices:
                for index in indices:
                    l_nums = l_nums[:index] + l_nums[index:index+2][::-1] + l_nums[index+2:]
                l_nums = order(l_nums, [i for i, cond in enumerate([tp in conditions for tp in pairwise(l_nums)]) if not cond])
            return l_nums

        s = [order(x, i) for x, i in s]
        print(sum([p[len(p)//2] for p in s]))
