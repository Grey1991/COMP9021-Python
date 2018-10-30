# Prompts the user for two numbers, say available_digits and desired_sum, and
# outputs the number of ways of selecting digits from available_digits
# that sum up to desired_sum.


import sys
from itertools import combinations

def solve(available_digits, desired_sum):
    s = str(available_digits)
    Ls = [int(i) for i in s]
    L = []
    for i in range(2,len(Ls)+1):
        com = combinations(Ls,i)
        for x in com:
            L.append(sum(x))
    num = L.count(desired_sum)
    return num

try:
    available_digits = abs(int(input('Input a number that we will use as available digits: ')))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    desired_sum = int(input('Input a number that represents the desired sum: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_solutions = solve(available_digits, desired_sum)
if nb_of_solutions == 0:
    print('There is no solution.')
elif nb_of_solutions == 1:
    print('There is a unique solution.')
else:
    print('There are {} solutions.'.format(nb_of_solutions))
