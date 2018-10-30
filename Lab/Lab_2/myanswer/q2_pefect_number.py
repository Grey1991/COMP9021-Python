# Prompts the user for an integer N and finds all perfect numbers up to N.
# Quadratic complexity, can deal with small values only.


import sys


try:
    N = int(input('Input an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
List = []
for i in range(2, N + 1):
    L = [1]
    for x in range(2,i//2+1):
        if i%x == 0:
            L.append(x)
    if sum(L) == i:
        List.append(i)
for x in List:
    print(x,'is a perfect number.')
            
        
