import sys
import os.path
from itertools import groupby
try:
    N = input('Please enter the name of the file you want to get data from: ')
    if os.path.exists(N):
        f = open(N)
        s = f.read()
        f.close()
        origin_list = s.split()
        L = [int(x) for x in origin_list]
        if len(L) <= 1 or L[0] <= 0:
            raise ValueError
        for i in range(len(L)-1):
            if  L[i+1] - L[i] <=0:
                raise ValueError
    else:
        raise EOFError
except ValueError:
    print('Sorry, input file does not store valid data.')
    sys.exit()
except EOFError:
    print('Sorry,there is no such file.')
    sys.exit()
print(L)
#============================
L = [int(x) for x in origin_list]
List2 = [L[n] - L[n - 1] for n in range(1, len(L))]
if len(set(List2)) == 1:
    print('The ride is perfect!\n'
          'The longest good ride has a length of: {}\n'
          'The minimal number of pillars to remove to build a perfect ride from the reat is: 0'.format(len(L)))
else:
    List3 = []
    for key,group in groupby(List2):
        List3.append(len(list(group)))
    length = max(List3)


