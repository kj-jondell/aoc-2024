import sys, re
import math

#i=sum([sum([math.prod([int(p) for p in x]) for x in re.findall(r'mul\((\d+),(\d+)\)', line)]) for line in sys.stdin]) # part 1

# part2
s = 0
enabled = True
for line in sys.stdin: # part 2
    for r in re.finditer(r"don't\(\)|mul\((\d+),(\d+)\)|do\(\)", line):
        if r.group(0) == "do()":
            enabled = True
        elif r.group(0) == "don't()":
            enabled = False
        elif enabled:
            s+=int(r.group(1))*int(r.group(2))
print(s)
