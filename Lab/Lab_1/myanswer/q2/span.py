from random import seed, randint
arg_for_seed = input('Input a seed for the random number generator: ')
try:
    arg_for_seed = int(arg_for_seed)
except ValueError:
    print('Input is not integer, give up.')
    sys.exit()
nb_for_elements = input('How many elements do you want to generate? ')
try:
    nb_for_elements = int(nb_for_elements)
except ValueError:
    print('Input is not interger, give up. ')
    sys.exit()
if nb_for_elements <= 0:
    print('Input should be strictly positive, give up. ')
    sys.exit()

seed(arg_for_seed)
L = [randint(0,99) for _ in range(nb_for_elements)]

print(L)
max_element = 99
min_element = 0

for i in L:
    if i > max_element:
        max_element = i
    if i < min_element:
        min_element = i
print(max_element - min_element)
