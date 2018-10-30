import time
start_time = time.time()
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
    for a in range(0,len(L)):
        for i in range(a,len(L)):
            S = S + L[i]
            if S <= N :
                n += 1
                if S in primeset:
                    if I < n :
                        I = n ; P = S
                    elif I == n and P < S :
                        P = S
        S = n = 0
    print(I, P)
    return I, P

N = int(input('input a number:'))
solution(N)

print("--- %s seconds ---" % (time.time() - start_time))