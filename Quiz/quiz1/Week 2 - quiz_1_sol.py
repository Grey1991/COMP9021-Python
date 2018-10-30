# Generates a list L of random nonnegative integers at most equal to some value
# input by the user, and of length also input by the user, and outputs a list
# consisting of the longest streak of consecutive occurrences of the same value in L,
# possibly looping around (as if the list was a ring). In the case multiple value
# have the longest streak of consecutive occurrences in L, then the smallest value is chosen.
#
# Written by Eric Martin for COMP9021


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
if len(set(L)) > 1:
    # special_pair records, for each streak, index in L where streak starts and negated streak value.
    # For example, with L = [1, 2, 3, 1, 1], special_pair is [(1, -2), (2, -3), (3, -1)].
    special_pairs = [(i, -L[i]) for i in range(len(L)) if L[i] != L[i - 1]]
    # Append first element to end, but adding length of L to index as if list was a ring.
    # With same example, special_pair becomes [(1, -2), (2, -3), (3, -1), (6, -2)].
    special_pairs.append((special_pairs[0][0] + len(L), special_pairs[0][1]))
    # Make special_pairs a list of pairs of the form: (streak length, negated streak value).
    # With same example, special_pair becomes [(1, -2), (1, -3), (3, -1)].
    special_pairs = [(special_pairs[i + 1][0] - special_pairs[i][0], special_pairs[i][1])
                                                                for i in range(len(special_pairs) - 1)]
    # Pick up longest length and for that length, largest negated value, so smallest value.
    best_streak = max(special_pairs)
    R = [-best_streak[1]] * best_streak[0]
    
print('\nThe longest streak of the same value is:')
print('  ', R)
