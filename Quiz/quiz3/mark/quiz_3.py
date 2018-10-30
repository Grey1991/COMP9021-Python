# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the number of
# parallelograms with horizontal sides. 
#
# Written by *** and Eric Martin for COMP9021


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
#=====================================================
def size_of_largest_parallelogram(X):
    from copy import deepcopy
    def max_bararea(L):
        area = 0
        List_histogram = L[0]
        for i in range(1, len(L)):
            List_histogram = [(L[i][j] + List_histogram[j]) * L[i][j] for j in range(len(List_histogram))]
            bar_number = 1

            for i in range(1, len(List_histogram)):
                if List_histogram[0] == 0 or List_histogram[0] ==1:
                    break
                if List_histogram[0] <= List_histogram[i]:
                    bar_number += 1
                else:
                    break
            if bar_number != 1:
                bar_area = bar_number * List_histogram[0]
            else:
                bar_area = 0
            if bar_area > area:
                area = bar_area
            bar_number = 1


            for i in range(1, len(List_histogram)-1):
                if List_histogram[i] == 0 or List_histogram[i] == 1:
                    continue
                for n in range(i + 1, len(List_histogram)):
                    if List_histogram[i] <= List_histogram[n]:
                        bar_number += 1
                    else:
                        break
                for m in range(i - 1, -1, -1):
                    if List_histogram[i] <= List_histogram[m]:
                        bar_number += 1
                    else:
                        break
                if bar_number != 1:
                    bar_area = bar_number * List_histogram[i]
                else:
                    bar_area = 0
                if bar_area > area:
                    area = bar_area
                bar_number = 1


            for i in range(len(List_histogram)-2, -1, -1):
                if List_histogram[-1] == 0 or List_histogram[-1] ==1:
                    break
                if List_histogram[-1] <= List_histogram[i]:
                    bar_number += 1
                else:
                    break
            if bar_number != 1:
                bar_area = bar_number * List_histogram[-1]
            else:
                bar_area = 0
            if bar_area > area:
                area = bar_area
        return area

    ##right===================================================
    def slidelist(L, code):
        slide = [[0]*(2*len(L[0])-1) for x in range(len(L))]
        if code == 1:
            for i in range(len(L)):
                for j in range(len(L[i])):
                    if L[i][j] != slide[i][i+j]:
                        slide[i][i+j]=L[i][j]
        else:
            for i in range(len(L)):
                for j in range(len(L[i])):
                    if L[i][j] != slide[i][len(L[0])-1+j-i]:
                        slide[i][len(L[0])-1+j-i]=L[i][j]
        return slide
    #========================================================
    def modify(L):
        for i in range(len(L)):
            for j in range(len(L[i])):
                if L[i][j] > 0:
                    L[i][j] = 1
        return L
#================================================
    M = modify(X)
    Mcp = deepcopy(M)
    Mcp_slide1 = slidelist(Mcp, 1)
    Mcp_slide2 = slidelist(Mcp, -1)
    size1 = max_bararea(Mcp)
    size2 = max_bararea(Mcp_slide1)
    size3 = max_bararea(Mcp_slide2)
    size = max(size1,size2,size3)
    return size
#===============================================
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


print('Here is the grid that has been generated:')
display_grid()
size = size_of_largest_parallelogram(grid)
if size:
    print('The largest parallelogram with horizontal sides has a size of', size, end='.\n')
else:
    print('There is no parallelogram with horizontal sides.')
