import sys
import numpy as np

lines = [[int(i) for i in line.strip()] for line in sys.stdin]
#rows = list(zip(*lines))
trailheads = [np.array([x, y]) for y, p in enumerate(lines) for x, v in enumerate(p) if v == 0]
width, height = len(lines[0]), len(lines)

#def walk(pos, val = 0, walks=set()):
#    if val == 9:
#        return "found"
#    for d in np.array([(1,0), (-1,0), (0,1), (0,-1)]):
#        dpos = pos+d
#        dx, dy = dpos
#        if ((dpos >= 0).all() and (dpos <= (width - 1, height - 1)).all()):
#            if (val + 1) == lines[dy][dx]:
#                if walk(dpos, val+1, walks) == "found":
#                    walks.add(tuple(dpos))
#    return walks
#
#print(sum([len(walk(trailhead, walks=set())) for trailhead in trailheads]))

def walk(pos, val = 0, walks=[]):
    if val == 9:
        return "found"
    for d in np.array([(1,0), (-1,0), (0,1), (0,-1)]):
        dpos = pos+d
        dx, dy = dpos
        if ((dpos >= 0).all() and (dpos <= (width - 1, height - 1)).all()):
            if (val + 1) == lines[dy][dx]:
                if walk(dpos, val+1, walks) == "found":
                    walks.append(dpos)
    return walks

print(sum([len(walk(trailhead, walks=[])) for trailhead in trailheads]))

