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
        for n in range(2, round(sqrt(N))+1):
            if prime_sieve[n]:
                for i in range(n*n, N + 1, n):
                    prime_sieve[i] = False
        return [x for x in range(2,N+1) if prime_sieve[x]]
    prime_list = get_primes(N)
    primeset=set(prime_list)
    prime_list = prime_list[::-1]
    T = sum(prime_list)
    S = 0
    for m in range(len(prime_list)-1,0,-1):
        if S <= N and S in primeset:
            break
        T = T - prime_list[m]
        S = T
        left = len(prime_list)- m
        if S <= N and S in primeset:
            P = S; I = m
            break
        else:
            for n in range(0,left):
                 S = S - prime_list[n] + prime_list[n+m]
                 if S <= N and S in primeset:
                     P = S;
                     I = m
                     break
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