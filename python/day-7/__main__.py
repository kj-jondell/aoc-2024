import sys
from operator import mul, add
import math
from itertools import combinations, product, pairwise
from functools import reduce
from collections import deque

lines = [(int(t), [int(x) for x in m.strip().split(" ")]) for t, m in [line.strip().split(":") for line in sys.stdin]]

possible = set()
for line in lines:
    ops = product([mul, add, lambda x, y: int(str(x)+str(y))], repeat=len(line[1])-1) # lambda should be used for part2 only
    for op in ops:
        deck = deque(op)
        nums = deque(line[1])
        running = nums.popleft()
        while deck:
            running = deck.pop()(running, nums.popleft())
            if running > line[0]:
                break
        if running == line[0]:
            possible.add(running)
            break
            #print(running, line[1], op)

print(sum(possible))
