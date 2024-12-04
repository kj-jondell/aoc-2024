import sys
import os

level = int(os.environ.get("LEVEL", 1))
in_d = ((int(n) for n in line.strip().split()) for line in sys.stdin)

match level:
################# PART 1 #################
    case 1: 
        print(sum(abs(dx-dy) for dx, dy in zip(*(sorted(n) for n in zip(*in_d))))) 
################# PART 2 #################
    case 2:
        left, right = zip(*in_d)
        print(sum(right.count(n)*n for n in left)) 
#print(sum(len(list(filter(lambda x: x==n, right)))*n for n in set(left))) 
