import sys
from collections import deque
from functools import reduce

line = next(sys.stdin).strip()

#f_stack = deque([i//2 if i % 2 == 0 else "." for i, d in enumerate(line) for x in range(int(d))])
#
#ch_sum, count = 0, 0
#while f_stack:
#    if (n := f_stack.popleft()) != ".":
#        ch_sum += count*int(n)
#        count += 1
#    else:
#        while f_stack and (n := f_stack.pop()) == ".":
#            pass
#        if n != ".":
#            ch_sum += count*int(n)
#            count += 1
#
#print(ch_sum)

oc = deque([(i, int(d)) for i, d in enumerate(line[::2])])
fr = deque([int(d) for d in line[1::2]])

print(oc, fr)
string = ""
f,t=oc.popleft()
print(str(f)*t)
next_free=fr.popleft()
print(next_free)
print(oc, fr)

for p in list(oc)[::-1]:
    if p[1] <= next_free:
        n = p
        break
oc.remove(n)
f,t = n
print(str(f)*t)

print(oc, fr)

