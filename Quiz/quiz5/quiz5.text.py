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
    for i in L:
        for n in i:
            print(int(n) , end= ' ')
        print()
    return max_spikes
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
print(colour_shapes(grid))
