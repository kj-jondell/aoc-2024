import sys
from collections import deque

def get_cond():
    while (line := next(sys.stdin).strip()):
        yield line.split("|")

conditions=[(int(x), int(y)) for x, y in get_cond()]

q=[[int(x.strip()) for x in line.split(",")] for line in sys.stdin]
s=[[u in conditions for u in zip(i, i[1:])] for i in q]

#s=sum([q[i][int(len(q[i])/2)] for i, k in enumerate(s) if False not in k])
#print(s)

s = [(q[i],[o for o,b in enumerate(k) if not b]) for i, k in enumerate(s) if False in k]

def order(l_nums, indices):
    if indices:
        for index in indices:
            l_nums = l_nums[:index] + l_nums[index:index+2][::-1] + l_nums[index+2:]
        l_nums = order(l_nums, [i for i, cond in enumerate([tp in conditions for tp in zip(l_nums, l_nums[1:])]) if not cond])
    return l_nums

s = [order(x, i) for x, i in s]
s=sum([p[int(len(p)/2)] for p in s])
print(s)
