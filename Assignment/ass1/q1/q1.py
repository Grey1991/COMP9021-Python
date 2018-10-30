import sys
from copy import deepcopy
def superpower_1(L, n):
    hero_list = deepcopy(L)
    hero_list.sort()
    low_hero = sum(x < 0 for x in hero_list)
    if n <= low_hero:
        for i in range(n):
            hero_list[i] = hero_list[i]*(-1)
            switch_hero = hero_list
    elif (n-low_hero)%2 == 0:
        switch_hero = [abs(x) for x in hero_list]
    else:
        hero_list = [abs(x) for x in hero_list]
        hero_list.sort()
        hero_list[0] = hero_list[0]*(-1)
        switch_hero = hero_list
    power = sum(switch_hero)
    return power

def superpower_2(L, n):
    hero_list = deepcopy(L)
    hero_list.sort()
    for i in range(n):
        hero_list[i] = hero_list[i] * (-1)
        switch_hero = hero_list
    power = sum(switch_hero)
    return power

def superpower_3(L,n):
    summation = [sum(L[i:i+n]) for i in range(0,len(L)-n+1)]
    power = sum(L) - 2*min(summation)
    return power

def superpower_4(L):
    summation = 0
    total = 0
    for i in L:
        if summation + i <= 0:
            summation = summation + i
            if summation < total:
                total = summation
        else:
            summation = 0
    power = sum(L) - 2*total
    return power

try:
    N = input('Please input the heroes\' powers: ')
    string = N.split()
    L = [int(x) for x in string]
except ValueError:
    print('Sorry, these are not valid power values.')
    sys.exit()
try:
    M = input('Please input the number of power flips: ')
    n = int(M)
    if n < 0 or n > len(L):
        raise ValueError
except ValueError:
    print('Sorry, this is not a valid number of power flips.')
    sys.exit()
if len(L) == 0:
    power1 = power2 = power3 = power4 = 0
elif n == 0:
    power1 = power2 = power3 = sum(L)
    power4 = superpower_4(L)
else:
    power1 = superpower_1(L, n)
    power2 = superpower_2(L, n)
    power3 = superpower_3(L, n)
    power4 = superpower_4(L)
print('Possibly flipping the power of the same hero many times, the greatest achievable power is {}.\n'
'Flipping the power of the same hero at most once, the greatest achievable power is {}.\n'
'Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {}.\n'
'Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is {}.'.format(power1, power2, power3, power4))

