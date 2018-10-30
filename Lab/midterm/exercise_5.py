import sys
from math import sqrt

def f(a, b):
    '''
    Won't be tested for b greater than 10_000_000
    
    >>> f(3, 3)
    The number of prime numbers between 3 and 3 included is 1
    >>> f(4, 4)
    The number of prime numbers between 4 and 4 included is 0
    >>> f(2, 5)
    The number of prime numbers between 2 and 5 included is 3
    >>> f(2, 10)
    The number of prime numbers between 2 and 10 included is 4
    >>> f(2, 11)
    The number of prime numbers between 2 and 11 included is 5
    >>> f(1234, 567890)
    The number of prime numbers between 1234 and 567890 included is 46457
    >>> f(89, 5678901)
    The number of prime numbers between 89 and 5678901 included is 392201
    '''
    if a <= 0 or b < a:
        sys.exit()
    nb_of_primes_between_a_and_b = 0
    # Insert your code here
    def is_prime(n):
        if n%2 ==0:
            return 0
        if n == 1 or n ==4:
            return 0
        if n ==2 or n ==3:
            return 1
        if n >4:
            for i in range(3,int(sqrt(n))+1,2):
                if n%i==0:
                    return 0
        return 1
    for i in range(a,b):
        if is_prime(i)==1:
            nb_of_primes_between_a_and_b += 1
            
    
    
    
    print('The number of prime numbers between', a, 'and', b, 'included is',
          nb_of_primes_between_a_and_b)



if __name__ == '__main__':
    import doctest
    doctest.testmod()
