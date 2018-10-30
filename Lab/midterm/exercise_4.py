import sys

def f(n):
    '''
    A number n is deficient if the sum of its proper divisors,
    1 included and itself excluded,
    is strictly smaller than n.
    
    >>> f(1)
    1 is deficient
    >>> f(2)
    2 is deficient
    >>> f(3)
    3 is deficient
    >>> f(6)
    6 is not deficient
    >>> f(29)
    29 is deficient
    >>> f(30)
    30 is not deficient
    >>> f(47)
    47 is deficient
    >>> f(48)
    48 is not deficient
    '''
    if n <= 0:
        sys.exit()
    # Insert your code here
    L=[]
    for i in range(1,n):
        if n%i ==0:
            L.append(i)
    if sum(L)<n:
        print(n,'is deficient')
    else:
        print(n,'is not deficient')

def g(a, b):
    '''
    a and b are amicable if
    - the sum of the proper divisors of a, 1 included and a excluded, is equal to b, and
    - the sum of the proper divisors of b, 1 included and b excluded, is equal to a.
    
    >>> g(220, 284)
    220 and 284 are amicable.
    >>> g(2924, 2620)
    2924 and 2620 are amicable.
    >>> g(1084, 1208)
    1084 and 1208 are not amicable.
    >>> g(5010, 5574)
    5010 and 5574 are not amicable.
    
    '''
    if a <= 0 or b <= 0:
        sys.exit()
    # Insert your code here
    L_a=[]
    L_b=[]
    for i in range(1,a):
        if a%i ==0:
            L_a.append(i)
    for x in range(1,b):
        if b%x ==0:
            L_b.append(x)
    if sum(L_a)==b and sum(L_b)==a:
        print('{} and {} are amicable.'.format(a,b))
    else:
        print('{} and {} are not amicable.'.format(a,b))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
