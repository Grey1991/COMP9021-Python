from random import seed, randint
from math import sqrt
from statistics import mean, median, pstdev
import sys
myseed = input('Input a seed for the random number generator: ')
try:
    myseed = int(myseed)
except ValueError:
    print('Input is not an interger, give up. ')
    sys.exit()
nb_for_elements = input('How many elements do you want to generate? ')
try:
    nb_for_elements = int(nb_for_elements)
except ValueError:
    print('Input is not an integer, giving up. ')
    sys.eixt()
if nb_for_elements <= 0 :
    print('Input should be strictly positive, giving up. ')
    sys.exit()
seed(myseed)
L = [randint(-50,50) for i in range(nb_for_elements)]

print('\nThe list is:',L)
print()
mean_my = sum(L)/len(L)
standard = sqrt(sum((x-mean_my)**2 for x in L)/len(L))
L.sort()
if nb_for_elements%2:
    median_my = L[(len(L)-1)//2]

else:
    median_my = (L[len(L)//2-1]+L[len(L)//2])/2
print('The mean is {:.2f}.'.format(mean_my))
print('The median is {:.2f}.'.format(median_my))
print('The standard deviation is {:.2f}.'.format(standard))
print('\nConfirming with functions from the statistics module:')
print('The mean is {:.2f}.'.format(mean(L)))
print('The median is {:.2f}.'.format(median(L)))
print('The standard deviation is {:.2f}.'.format(pstdev(L)))
