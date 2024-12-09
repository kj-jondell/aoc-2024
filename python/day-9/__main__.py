import sys
from collections import deque
from functools import reduce

line = next(sys.stdin).strip()

f_stack = deque([i//2 if i % 2 == 0 else "." for i, d in enumerate(line) for x in range(int(d))])

print(f_stack)
ch_sum, count = 0, 0
while f_stack:
    if (n := f_stack.popleft()) != ".":
        ch_sum += count*int(n)
        count += 1
    else:
        while f_stack and (n := f_stack.pop()) == ".":
            pass
        if n != ".":
            ch_sum += count*int(n)
            count += 1

print(ch_sum)
