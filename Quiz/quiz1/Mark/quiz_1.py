# Generates a list L of random nonnegative integers at most equal to some value
# input by the user, and of length also input by the user, and outputs a list
# consisting of the longest streak of consecutive occurrences of the same value in L,
# possibly looping around (as if the list was a ring). In the case multiple value
# have the longest streak of consecutive occurrences in L, then the smallest value is chosen.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randint


try:
    arg_for_seed, length, max_value = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
print('\nThe generated list is:')
print('  ', L)

R = L
#input your code
def longestvaluelist(R):
    R = R*2
    value_len = 1
    current_len = 1

    if R == []:
        return []
    else:
        value = min(R)
        for i in range(1,len(R)):

            if R[i] == R[i-1]:
                current_value = R[i]
                current_len += 1
                if value_len < current_len:
                    value_len = current_len
                    value = current_value
                elif value_len == current_len and value > current_value:
                    value = current_value
            else:
                current_len = 1
    if value_len == len(R):
        value_len = len(R)/2
    R = [value]*int(value_len)
    return R
R = longestvaluelist(R)



print('\nThe longest streak of the same value is:')
print('  ', R)