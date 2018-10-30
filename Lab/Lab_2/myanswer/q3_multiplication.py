# Decodes all multiplications of the form
#
#                        e  d  c
#                   x       b  a
#                     ----------
#                     *  *  *  *
#                     *  *  *
#                     ----------
#                     *  *  *  *
#
# such that the sum of all digits in all 4 columns is constant.


for x in range(100, 1000):
    for y in range(10, 100):
        a = y%10; b = y//10; c = x%10; d = (x//10)%10; e = x//100; f = x*y
        if f < 10000 and x * a >= 1000:            
            n = a + c + (f%10)*2
            if ((f//10)%10)*2 + d +b == n and ((f//100)%10)*2 + e == n and (f//1000)*2 == n:
                print('{} * {} = {}, all columns adding up to {}.'.format(x,y,x*y,n))
            
            
