import os.path
import sys
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
            if L1[i] <= L2[i] or L1[i] ==0 or L2[i] == 0:
                raise ValueError
except EOFError:
    print('Sorry, there is no such file.')
    sys.exit()
except ValueError:
    print('Sorry, input file does not store valid data.')
    sys.exit()

print(L1,L2)


