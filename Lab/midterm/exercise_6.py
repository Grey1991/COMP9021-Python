''' Hint in the form of syntactic notes:
    str(n) converts a number n to a string.
    set(s) converts a string s to a set of characters.
    len() returns the number of elements in its argument, e.g, a string, or a set.
    
    S1 | S2 returns the union of two sets S1 and S2.

'''

import sys

def f(a, b):
    '''
    Finds all numbers i and j with a <= i <= j <= b such that
    every digit occurs at most once in i, j and i * j.
    Outputs the solutions from smallest i to largest i,
    and for a given i from smallest j to largest j.
    
    >>> f(32, 49)
    32 * 49 = 1568 is a solution
    38 * 42 = 1596 is a solution
    >>> f(30, 50)
    32 * 49 = 1568 is a solution
    38 * 42 = 1596 is a solution
    >>> f(40, 80)
    48 * 65 = 3120 is a solution
    52 * 79 = 4108 is a solution
    53 * 76 = 4028 is a solution
    58 * 64 = 3712 is a solution
    59 * 68 = 4012 is a solution
    59 * 78 = 4602 is a solution
    68 * 74 = 5032 is a solution
    >>> f(50, 110)
    52 * 79 = 4108 is a solution
    53 * 76 = 4028 is a solution
    53 * 92 = 4876 is a solution
    57 * 86 = 4902 is a solution
    58 * 64 = 3712 is a solution
    59 * 68 = 4012 is a solution
    59 * 78 = 4602 is a solution
    59 * 108 = 6372 is a solution
    62 * 87 = 5394 is a solution
    68 * 74 = 5032 is a solution
    69 * 108 = 7452 is a solution
    72 * 95 = 6840 is a solution
    74 * 85 = 6290 is a solution
    '''
    if a <= 0 or b < a:
        sys.exit()
    # Insert your code here

    for i in range(a,b):
        str_i = str(i)
        set_i = {int(str_i[x]) for x in range(len(str_i))}
        if len(str_i) != len(set_i):
            continue
        for j in range(i,b+1):           
            str_j = str(j)
            set_j = {int(str_j[x]) for x in range(len(str_j))}
            if len(str_j) != len(set_j):
                continue
            set_a = set_i | set_j
            if len(set_a) != len(set_i)+len(set_j):
                continue
            str_ij = str(i*j)
            set_ij = {int(str_ij[x]) for x in range(len(str_ij))}            
            if len(set_ij) != len(str_ij):
                continue
            set_b = set_ij | set_a
            if len(set_b) == len(set_a)+len(set_ij):
                print('{} * {} = {} is a solution'.format(i,j,i*j))
    
                

if __name__ == '__main__':
    import doctest
    doctest.testmod()
