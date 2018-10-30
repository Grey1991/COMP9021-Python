# Say that two strings s_1 and s_2 can be merged into a third
# string s_3 if s_3 is obtained from s_1 by inserting
# arbitrarily in s_1 the characters in s_2, respecting their
# order. For instance, the two strings ab and cd can be merged
# into abcd, or cabd, or cdab, or acbd, or acdb..., but not into
# adbc nor into cbda.
#
# Prompts the user for 3 strings and displays the output as follows:
# - If no string can be obtained from the other two by merging,
# then the program outputs that there is no solution.
# - Otherwise, the program outputs which of the strings can be obtained
# from the other two by merging.

from itertools import permutations

def can_merge(string_1, string_2, string_3):
    L_1 = [(string_1[i],i,1) for i in range(len(string_1))]
    L_2 = [(string_2[i],i,2) for i in range(len(string_2))]
    L = L_1+L_2
    P = permutations(L,len(string_3))    
    for i in P:
        m = -1
        n = -1
        s = 1
        for x in i:
            if x[2] == 1:
                if x[1] == m+1:
                    m += 1
                else:
                    s = 0
                    break
            else:
                if x[1] == n+1:
                    n += 1
                else:
                    s = 0
                    break
        if s == 1:
            str_made = ''
            for x in i:
                str_made += x[0]
                if str_made == string_3:
                    return True
    return False


strings = []
ordinals = 'first', 'second', 'third'
for i in ordinals:
    strings.append(input('Please input the {} string: '.format(i)))

last = 0
if len(strings[1]) > len(strings[0]):
    last = 1
if len(strings[2]) > len(strings[last]):
    last = 2
if last == 0:
    first, second = 1, 2
elif last == 1:
    first, second = 0, 2
else:
    first, second = 0, 1
if (len(strings[last]) != len(strings[first]) + len(strings[second]) or
                                          not can_merge(strings[first], strings[second], strings[last])):
    print('No solution')
else:
    print('The {} string can be obtained by merging the other two.'.format(ordinals[last]))


    
