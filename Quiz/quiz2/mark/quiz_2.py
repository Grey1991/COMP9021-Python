# Prompts the user for an integer N at least equal to 5,
# computes the largest number l >= 1 such that l consecutive prime numbers
# add up to a prime number at most equal to N,
# and outputs l and the larger such prime number.
#
# Written by *** and Eric Martin for COMP9021
import sys
def solution(N):
    from math import sqrt
    def get_primes(N):
        prime_sieve = [True] * (N + 1)
        for n in range(2, round(sqrt(N)) + 1):
            if prime_sieve[n]:
                for i in range(n * n, N + 1, n):
                    prime_sieve[i] = False
        return [x for x in range(2, N + 1) if prime_sieve[x]]
    L = get_primes(N)
    primeset = set(L)
    S = n = I = P = 0
    for a in range(0,len(L)-1):
        if L[a]+L[a+1] > N:
            break
        for i in range(a,len(L)):
            S = S + L[i]
            if S <= N :
                n += 1
                if S in primeset:
                    if I < n :
                        I = n ; P = S
                    elif I == n and P < S :
                        P = S
            else:
                break
        S = n = 0
    return I, P
try:
    N = int(input('Enter an integer at least equal to 5: '))
    if N < 5:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
#import time
#start_time = time.time()

max_length, candidate = solution(N)
if max_length:
    print('The largest sequence of consecutive primes that add up\n  '
          'to a prime P equal to {} at most has a length of {}.\n'
          'The largest such P is {}.'.format(N, max_length, candidate))
#print("--- %s seconds ---" % (time.time() - start_time))
