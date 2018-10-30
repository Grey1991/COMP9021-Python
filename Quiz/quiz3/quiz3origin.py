from random import seed, randrange
import sys

dim = 10


def display_grid():
    for i in range(dim):
        print('    ', end='')
        for j in range(dim):
            print(' 1', end='') if grid[i][j] else print(' 0', end='')
        print()
    print()


#def size_of_largest_parallelogram():
    #pass
    # Replace pass above with your code



# Possibly add code for other functions


try:
    for_seed, n = [int(i) for i in
                   input('Enter two integers, the second one being strictly positive: ').split()]
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randrange(n) for _ in range(dim)] for _ in range(dim)]


#print('Here is the grid that has been generated:')
##display_grid()
#size = size_of_largest_parallelogram()
#if size:
    #print('The largest parallelogram with horizontal sides has a size of ', size, end='.\n')
#else:
    #print('There is no parallelogram with horizontal sides.')

