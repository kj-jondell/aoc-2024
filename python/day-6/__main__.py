import sys, re
from collections import deque
from itertools import pairwise, islice, product

rows = [line for line in map(str.strip, sys.stdin)]
cols = ["".join(row) for row in zip(*rows)]

for y, line in enumerate(rows):
    if m := re.search(r'\^', line):
        x = m.start()
        break

positions = []
while True:
    if m := re.search(r'#', cols[x][:y]):
        positions += [(x, ny) for ny in range(y,m.end(),-1)]
        y = m.end()
    else:
        break

    if m := re.search(r'#', rows[y][x+1:]):
        positions += [(nx, y) for nx in range(x, x+m.start(),1)]
        x += m.start()
    else:
        break

    if m := re.search(r'#', cols[x][y+1:]):
        positions += [(x, ny) for ny in range(y, y+m.start(),1)]
        y += m.start()
    else:
        break

    if m := re.search(r'#', rows[y][:x]):
        positions += [(nx, y) for nx in range(x,m.end(),-1)]
        x = m.end()
    else:
        positions += [(nx, y) for nx in range(x,m.end(),-1)]
        break

print(positions)

#x, y = init_pos
#positions = []
#stones = []
#try:
#    while True:
#        d=iter(cols[x][:y][::-1])
#        while (r:=next(d)) != "#":
#            positions.append((x,y))
#            y -= 1
#        stones.append((x, y-1))
#
#        d=iter(rows[y][x+1:])
#        while (r:=next(d)) != "#":
#            positions.append((x,y))
#            x += 1
#        stones.append((x+1, y))
#
#        d=iter(cols[x][y+1:])
#        while (r:=next(d)) != "#":
#            positions.append((x,y))
#            y += 1
#        stones.append((x, y+1))
#
#        d=iter(rows[y][:x][::-1])
#        while (r:=next(d)) != "#":
#            positions.append((x,y))
#            x -= 1
#        stones.append((x-1, y))
#        positions.append((x,y))
#except:
#    print(len(set(positions))+1)
#    print(positions)
#
#for chunk in [stones[x:x+3] for x in range(len(stones)-2)]:
#    print(chunk)
#print(len(stones))
#print([(y[0]-x[0], y[1]-x[1]) for x, y in pairwise(stones)])

#print([(stones[x:x+3]+[((stones[x+(x%3)][0]-stones[x+((x+1)%3)][0]+stones[x+((x+2)%3)][0])%10, (stones[x+(x%3)][1]-stones[x+((x+1)%3)][1]+stones[x+((x+2)%3)][1]) % 10 )]) for x in range(len(stones)-2)])
