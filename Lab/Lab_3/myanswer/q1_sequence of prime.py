# Finds all sequences of consecutive prime 5-digit numbers,
# say (a, b, c, d, e, f), such that
# b = a + 2, c = b + 4, d = c + 6, e = d + 8, and f = e + 10.


from math import sqrt


def is_prime(n):
    for i in range(3,int(sqrt(n))+1,2):
        if n%i == 0:
            return 0
    return 1


print('The solutions are:\n')
# The list of all even i's such that a + i is one of a, b, c, d, e, f.
good_leaps = tuple(sum(range(0, k, 2)) for k in range(2, 13, 2))

for i in range(10001,99970,2):
    if all(is_prime(i+x)==1 for x in good_leaps) and all(not is_prime(i+n) for n in range(2,30,2) if n != 2 and n!= 6 and n!=12 and n!=20 and n!=30):
        for x in good_leaps[:-1]:
            print(i+x,end='  ')
        print(i+30)

        
            


