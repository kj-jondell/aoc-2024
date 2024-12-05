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
k = 0
for x, i in s:
    while True:
        for u in i:
            x = x[:u] + x[u:u+2][::-1] + x[u+2:]
        s=[u in conditions for u in zip(x, x[1:])]
        if False not in s:
            k += x[int(len(x)/2)]
            break
        else:
            i = [o for o,b in enumerate(s) if not b]
print(k)
