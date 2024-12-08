import sys, re
from collections import deque
from itertools import pairwise, islice

rows = [tuple(line.strip()) for line in sys.stdin]
cols = list(zip(*rows))

init_pos = (0, 0) # col, row
for col, c in enumerate(cols):
    for row, p in enumerate(c):
        if p == "^":
            init_pos = (col, row)

col, row = init_pos
positions = set()
stones = []
try:
    while True:
        d=iter(cols[col][:row][::-1])
        while (r:=next(d)) != "#":
            positions.add((col,row))
            row -= 1
        stones.append((col, row-1))

        d=iter(rows[row][col+1:])
        while (r:=next(d)) != "#":
            positions.add((col,row))
            col += 1
        stones.append((col+1, row))

        d=iter(cols[col][row+1:])
        while (r:=next(d)) != "#":
            positions.add((col,row))
            row += 1
        stones.append((col, row+1))

        d=iter(rows[row][:col][::-1])
        while (r:=next(d)) != "#":
            positions.add((col,row))
            col -= 1
        stones.append((col-1, row))
        positions.add((col,row))
except:
    print(len(positions)+1)

print(stones, init_pos)
print(len(stones))
#print([(y[0]-x[0], y[1]-x[1]) for x, y in pairwise(stones)])

print([(stones[x:x+3]+[((stones[x+(x%3)][0]-stones[x+((x+1)%3)][0]+stones[x+((x+2)%3)][0])%10, (stones[x+(x%3)][1]-stones[x+((x+1)%3)][1]+stones[x+((x+2)%3)][1]) % 10 )]) for x in range(len(stones)-2)])
