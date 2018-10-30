# Prompts the user to input an integer N at least equal to 10 and computes N!
# in three different ways.


import sys
from math import factorial


def first_computation(x):
    nb_of_trailing_0s = 0
    for i in range(x):
        if not x%10:
            x = x//10
            nb_of_trailing_0s += 1
        else:
            break
    return nb_of_trailing_0s

def second_computation(x):
    x = str(x)
    nb = 0
    for i in range(-1,-len(x),-1):
        if x[i] == '0':
            nb += 1
        else:
            break
    return nb
        
    
def third_computation(x):
    nb_of_trailing_0s = 0
    power_of_five = 5
    while power_of_five <= x:
        for i in range(1,x+1):
            if i%power_of_five == 0:
                nb_of_trailing_0s += 1
            
        power_of_five = power_of_five*5
        print(nb_of_trailing_0s)
    return nb_of_trailing_0s

try:
    the_input = int(input('Input a nonnegative integer: '))
    if the_input < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

the_input_factorial = factorial(the_input)
print(f'Computing the number of trailing 0s in {the_input}! by dividing by 10 for long enough:',
      first_computation(the_input_factorial))
print(f'Computing the number of trailing 0s in {the_input}! by converting it into a string:',
      second_computation(str(the_input_factorial)))
print(f'Computing the number of trailing 0s in {the_input}! the smart way:',
      third_computation(the_input))
