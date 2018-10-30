import os.path
import sys
from copy import deepcopy
from itertools import groupby
#==================================================
try:
    N = input('Please enter the name of the file you want to get data from: ')
    if not os.path.exists(N):
        raise EOFError
    else:
        f = open(N)
        s = f.read()
        f.close()
        List = s.strip().split('\n')
        List_origin = [x for x in List if x != '']
        if len(List_origin) != 2:
            raise ValueError
        L1_origin = List_origin[0].split()
        L2_origin = List_origin[1].split()
        L1 = [int(x) for x in L1_origin]
        L2 = [int(x) for x in L2_origin]
        if len(L1) != len(L2) or len(L1) < 2:
            raise ValueError
        for i in range(len(L1)):
            if L1[i] <= L2[i]:
                raise ValueError
except EOFError:
    print('Sorry, there is no such file.')
    sys.exit()
except ValueError:
    print('Sorry, input file does not store valid data.')
    sys.exit()
#==================================================
N = [0]*len(L1)
M = [deepcopy(N) for i in range(max(L1)-min(L2)+2)]
for i in range(len(L1)):
    for j in range(max(L1)-L1[i]+1,max(L1)-L2[i]+1):
        M[j][i] = 1
#===========================================
max_west_distance = 0
for i in range(len(M)):
    west_distance = 0
    for j in range(len(M[i])):
        if M[i][j] == 1:
            west_distance += 1
        else:
            break
    if west_distance > max_west_distance:
        max_west_distance = west_distance
#===========================================
max_tunnel_length = 0
for i in range(len(M)):
    tunnel_length = []
    for key,group in groupby(M[i]):
        tunnel_length.append(len(list(group))*key)
    if max(tunnel_length) > max_tunnel_length:
        max_tunnel_length = max(tunnel_length)
#==================================================
print('From the west, one can into the tunnel over a distance of {}\n'
      'Inside the tunnel, one can into the tunnel over a maximum distance of {}'.format(max_west_distance,max_tunnel_length))
