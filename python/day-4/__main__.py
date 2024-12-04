import sys, re

i_d = [line.strip() for line in sys.stdin]
s = 0

#part 1
s = sum([len(list(filter(lambda p: p, [line[i:i+4] == "XMAS" or line[i:i+4] == "SAMX" for i in range(len(line)-3)]))) for line in i_d]) + sum([len(list(filter(lambda p: p, [line[i:i+4] == ('X','M','A','S') or line[i:i+4] == ('S','A','M','X') for i in range(len(line)-3)]))) for line in zip(*i_d)]) + sum([len(list(filter(lambda x: x==('X','M','A','S') or x==('S','A','M','X'), zip(i_d[i],i_d[i+1][1:], i_d[i+2][2:],i_d[i+3][3:])))) + len(list(filter(lambda x: x==('X','M','A','S') or x==('S','A','M','X'), zip(i_d[i][3:],i_d[i+1][2:], i_d[i+2][1:],i_d[i+3])))) for i in range(len(i_d)-3)])
#print(s)

#part 2
#for i in range(len(i_d)-2):
#    p = list(zip(i_d[i],i_d[i+1][1:], i_d[i+2][2:]))
#    q = list(zip(i_d[i][2:],i_d[i+1][1:], i_d[i+2]))
#    for index,u in enumerate(p):
#        if (u == ('M','A','S') or u == ('S','A','M')) and (q[index] == ('M','A','S') or q[index] == ('S','A','M')):
#            s += 1
print(s)
