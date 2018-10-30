# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out".
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' 1', end = '') if grid[i][j] else print(' 0', end = '')
        print()
    print()


# Returns the number of shapes we have discovered and "coloured".
# We "colour" the first shape we find by replacing all the 1s that make it with 2.
# We "colour" the second shape we find by replacing all the 1s that make it with 3.
def colour_shapes(L):
    pass
    # Replace pass above with your code
    nb_of_shapes = 1
    max_spikes = 0
    for i in range(10):
        for j in range(10):
            if L[i][j] == 1:
                nb_of_shapes +=1
                L[i][j] = nb_of_shapes
                nb_of_spikes = 0
                stack = [[i,j]]

                for x in stack:
                    if len(stack) ==2:
                        nb_of_spikes +=1
 #===========up==============
                    nb_of_neighbour_1 = 0
                    nb_of_neighbour_shapes = 0
                    if x[0]-1 >=0 :
                        if L[x[0]-1][x[1]] == 1:
                            stack.append([x[0]-1,x[1]])
                            L[x[0]-1][x[1]] = nb_of_shapes
                            nb_of_neighbour_1 += 1
                        elif L[x[0]-1][x[1]] == nb_of_shapes:
                            nb_of_neighbour_shapes += 1
 #===========down==============
                    if x[0] + 1 < 10:
                        if L[x[0] + 1][x[1]] == 1:
                            stack.append([x[0] + 1, x[1]])
                            L[x[0] + 1][x[1]] = nb_of_shapes
                            nb_of_neighbour_1 += 1
                        elif L[x[0]+1][x[1]] == nb_of_shapes:
                            nb_of_neighbour_shapes += 1
#===========left==================
                    if x[1]-1 >=0:
                        if L[x[0]][x[1]-1] == 1:
                            stack.append([x[0] , x[1] - 1])
                            L[x[0]][x[1]-1] = nb_of_shapes
                            nb_of_neighbour_1 += 1
                        elif L[x[0]][x[1]-1] == nb_of_shapes:
                            nb_of_neighbour_shapes += 1
#===========right===============
                    if x[1]+1<10:
                        if L[x[0]][x[1]+1]==1:
                            stack.append([x[0], x[1] + 1])
                            L[x[0]][x[1]+1] = nb_of_shapes
                            nb_of_neighbour_1 += 1
                        elif L[x[0]][x[1]+1] == nb_of_shapes:
                            nb_of_neighbour_shapes += 1
                    if nb_of_neighbour_1 == 0 and nb_of_neighbour_shapes == 1:
                        nb_of_spikes += 1
                if len(stack) == 1:
                    nb_of_spikes = 1

                if nb_of_spikes > max_spikes:
                    max_spikes = nb_of_spikes
    return max_spikes


def max_number_of_spikes(nb_of_shapes):
    pass
    return nb_of_shapes
    # Replace pass above with your code


# Possibly define other functions here    


try:
    for_seed, n = [int(i) for i in
                        input('Enter two integers, the second one being strictly positive: ').split()]
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randrange(n) != 0 for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
nb_of_shapes = colour_shapes(grid)
print('The maximum number of spikes of some shape is equal to',nb_of_shapes)
