import sys

def get_cond():
    while (line := next(sys.stdin).strip()):
        yield line.split("|")

conditions=[(int(x), int(y)) for x, y in get_cond()]

q=[[int(x.strip()) for x in line.split(",")] for line in sys.stdin]
s=[[u in conditions for u in zip(i, i[1:])] for i in q]

s=sum([q[i][int(len(q[i])/2)] for i, k in enumerate(s) if False not in k])
print(s)
