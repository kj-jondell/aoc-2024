import sys
import os

i_d = [line.strip() for line in sys.stdin]
level = int(os.environ.get("LEVEL", 1))

match level:
################ Part 1 ################
    case 1:
        print(sum([len(list(filter(lambda p: p, [line[i:i+4] == "XMAS" or line[i:i+4] == "SAMX" for i in range(len(line)-3)]))) for line in i_d]) + sum([len(list(filter(lambda p: p, [line[i:i+4] == ('X','M','A','S') or line[i:i+4] == ('S','A','M','X') for i in range(len(line)-3)]))) for line in zip(*i_d)]) + sum([len(list(filter(lambda x: x==('X','M','A','S') or x==('S','A','M','X'), zip(i_d[i],i_d[i+1][1:], i_d[i+2][2:],i_d[i+3][3:])))) + len(list(filter(lambda x: x==('X','M','A','S') or x==('S','A','M','X'), zip(i_d[i][3:],i_d[i+1][2:], i_d[i+2][1:],i_d[i+3])))) for i in range(len(i_d)-3)]))
################ Part 2 ################
    case 2:
        print(sum([(len(list(filter(lambda u: (u[0] == ('M','A','S') or u[0] == ('S','A','M')) and (u[1] == ('M','A','S') or u[1] == ('S','A','M')), zip(zip(i_d[i],i_d[i+1][1:], i_d[i+2][2:]), zip(i_d[i][2:],i_d[i+1][1:], i_d[i+2])))))) for i in range(len(i_d)-2)]))
