'''
Every strictly positive integer N can be uniquely coded as a string sigma
of 0's and 1's ending with 1, so of the form b_2b_3...b_k with k >= 2 and b_k = 1,
such that N is the sum of all F_i's, 2 <= i <= k, with b_i = 1.

Moreover:
- there are no two successive occurrences of 1 in sigma;
- F_k is the largest Fibonacci number that fits in N, and
  if j is the largest integer in {2,...,k-1} such that b_j = 1
  then F_j is the largest Fibonacci number that fits in N - F_k, and
  if i is the largest integer in {2,...,j-1} such that b_i = 1
  then F_i is the largest Fibonacci number that fits in  N - F_k - F_j...

Also, every string of 0's and 1's ending in 1 and having no two
successive occurrences of 1's is a code of a strictly positive integer
according to this coding scheme. For instance:
- There is only one string of 0's and 1's of length 1 ending in 1 and
  having no two successive occurrences of 1's; it is 1, and it codes 1.
- There is only one string of 0's and 1's of length 2 ending in 1 and
  having no two successive occurrences of 1's; it is 01, and it codes 2.
- The strings of 0's and 1's of length 3 ending in 1 and having no two successive occurrences
  of 1's are 001 and 101 and they code 3 and 4, respectively.
- The strings of 0's and 1's of length 4 ending in 1 and having no two successive occurrences
  of 1's are 0001, 1001 and 0101 and they code 5, 6 and 7, respectively.
- The strings of 0's and 1's of length 5 ending in 1 and having no two successive occurrences
  of 1's are 00001, 10001, 01001, 00101 and 10101 and they code 8, 9, 10, 11 and 12, respectively.
- ...

The Fibonacci code of N adds 1 at the end of sigma; the resulting string then ends in two 1's,
therefore marking the end of the code, and allowing one to let one string code a finite sequence
of strictly positive integers. For instance, 00101100111011 codes (11,3,4).
'''


def encode(n):
    '''
    Retuns the Fibonacci code of n, meant to be a strictly positive integer.
    
    >>> encode(1)
    '11'
    >>> encode(2)
    '011'
    >>> encode(3)
    '0011'
    >>> encode(4)
    '1011'
    >>> encode(5)
    '00011'
    >>> encode(6)
    '10011'
    >>> encode(7)
    '01011'
    >>> encode(8)
    '000011'
    >>> encode(9)
    '100011'
    >>> encode(10)
    '010011'
    >>> encode(11)
    '001011'
    >>> encode(12)
    '101011'
    >>> encode(13)
    '0000011'
    >>> encode(14)
    '1000011'
    
    '''
    L = [0,1]
    while L[-1] <= n:
        L.append(L[-1]+L[-2])
    L.pop()
    S = [0]*len(L)
    for i in range(len(L)-1,-1,-1):
        if n >= L[i]:
            n = n- L[i]
            S[i]=1
        if n == 0:
            break
    encode = ''
    for i in range(2,len(S)):
        encode += str(S[i])
    encode += '1'
    return encode
    

def decode(code):
    '''
    The argument is meant to be a string of 0's and 1's.
    Returns 0 if the argument cannot be a Fibonacci code;
    otherwise returns the integer argument is the Fibonacci code of.
    
    >>> decode('1')
    0
    >>> decode('01')
    0
    >>> decode('111')
    0
    >>> decode('100011011')
    0
    >>> decode('11')
    1
    >>> decode('011')
    2
    >>> decode('0011')
    3
    >>> decode('1011')
    4
    >>> decode('00011')
    5
    >>> decode('10011')
    6
    >>> decode('01011')
    7
    >>> decode('000011')
    8
    >>> decode('100011')
    9
    >>> decode('010011')
    10
    >>> decode('001011')
    11
    >>> decode('101011')
    12
    >>> decode('0000011')
    13
    >>> decode('1000011')
    14
    
    '''
    if len(code)<2:
        return 0
    if code[-2] != '1':
        return 0
    L = [0,1]
    for i in range(len(code)-1):
        L.append(L[-1]+L[-2])
    decode = 0
    num = 0
    for i in range(len(code)-1):
        if code[i] == '1':
            num += 1
            if num >1:
                return 0
            decode += L[i+2]
        else:
            num = 0
    return decode
    
   
if __name__ == '__main__':
    import doctest
    doctest.testmod()
