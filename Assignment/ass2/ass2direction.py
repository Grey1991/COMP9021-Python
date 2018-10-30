import sys, os
from argparse import ArgumentParser

def direction(point_1,point_2):
    if point_1[0] == point_2[0]-1 and point_1[1] == point_2[1]:
        origin_direction = 0
    if point_1[0] == point_2[0]-1 and point_1[1] == point_2[1]+1:
        origin_direction = 1
    if point_1[0] == point_2[0] and point_1[1] == point_2[1]+1:
        origin_direction = 2
    if point_1[0] == point_2[0]+1 and point_1[1] == point_2[1]+1:
        origin_direction = 3
    if point_1[0] == point_2[0]+1 and point_1[1] == point_2[1]:
        origin_direction = 4
    if point_1[0] == point_2[0]+1 and point_1[1] == point_2[1]-1:
        origin_direction = 5
    if point_1[0] == point_2[0] and point_1[1] == point_2[1]-1:
        origin_direction = 6
    if point_1[0] == point_2[0]-1 and point_1[1] == point_2[1]-1:
        origin_direction = 7
    return origin_direction

def find_neighbour_1(n, m, L):
    enter_direction = direction(n,m)
    neighbour_points = [[m[0]-1,m[1]],[m[0]-1,m[1]+1],[m[0],m[1]+1],[m[0]+1,m[1]+1],[m[0]+1,m[1]],[m[0]+1,m[1]-1],[m[0],m[1]-1],[m[0]-1,m[1]-1]]
    neighbour_1_point = None
    for i in range(2,8):
        x = neighbour_points[(enter_direction+i)%8][0]
        y = neighbour_points[(enter_direction+i)%8][1]
        if 0 <= x < len(L) and 0 <= y < len(L[0]) and L[x][y] == 1:
            neighbour_1_point = [x, y]
            break
    return neighbour_1_point

def shape_analyse(L):
    enter_direction_list = [direction(L[i-1],L[i]) for i in range(len(L))]
    n=0;m=0
    for i in enter_direction_list:
        if i%2 == 0:
            n += 1
        else:
            m += 1
    if n ==0 :
        Perimeter = str(m)+'*sqrt(.32)'
    elif m == 0:
        Perimeter = '%.1f'%float(n*0.4)
    else:
        Perimeter = '%.1f'%float(n*0.4) +' + '+str(m)+'*sqrt(.32)'
#======================================================================================
    area = 1/2*0.16*sum((L[i-1][1]+1)*(L[i][0]+1)-(L[i-1][0]+1)*(L[i][1]+1) for i in range(len(L)))
#====================================================================================
    if sum((enter_direction_list[i]-enter_direction_list[i-1])%8 for i in range(len(enter_direction_list))) == 8:
        convex = 'yes'
    else:
        convex = 'no'
#=====================================================================================
    inflection_points = [L[x-1] for x in range(len(L)) if enter_direction_list[x] != enter_direction_list[x - 1]]
    if len(inflection_points) %2 != 0:
        invariant = 1
    else:
        middle_x = (inflection_points[0][0] + inflection_points[len(inflection_points)//2][0])/2
        middle_y = (inflection_points[0][1] + inflection_points[len(inflection_points)//2][1])/2
        if all(middle_x == (inflection_points[x][0] + inflection_points[len(inflection_points)//2+x][0])/2 \
                and middle_y == (inflection_points[x][1] + inflection_points[len(inflection_points)//2+x][1])/2 for\
               x in range(len(inflection_points) // 2)):
            if len(inflection_points) %4 ==0 and \
                    all([middle_y-inflection_points[x][1] + middle_x,inflection_points[x][0]-middle_x+middle_y] in inflection_points for x in range(len(inflection_points)//4)):
                invariant = 4
            else:
                invariant = 2
        else:
            invariant = 1
    return Perimeter,area,convex,invariant

def point_in_shape(point,shape):
    count = 0
    enter_direction_list = [direction(shape[i - 1], shape[i]) for i in range(len(shape))]
    inflection_points = [shape[x-1] for x in range(len(shape)) if enter_direction_list[x] != enter_direction_list[x - 1]]
    shape2 = [shape[x] for x in range(len(shape)-1) if shape[x][0] != shape[x+1][0]]
    shape2.append(shape[-1])
    for i in range(len(shape2)):
        if shape2[i][0] == point[0] and shape2[i][1] > point[1]:
            if shape2[i] in inflection_points:
                if i+1 == len(shape2):
                    if (shape2[i-1][0]-point[0])*(shape2[0][0]-point[0]) < 0:
                        count += 1
                elif (shape2[i-1][0]-point[0])*(shape2[i+1][0]-point[0]) < 0:
                    count += 1
            else:
                count += 1
    if count % 2 == 1:
        return True
    else:
        return False
#===================main====================================
# parser = ArgumentParser()
# parser.add_argument('--file', dest = 'file_name', required = True)
# parser.add_argument('-print', dest = 'print', action = 'store_true')
# args = parser.parse_args()
#
# file_name = args.file_name.split('.')[0].split('/')[-1]
# tex_file_name = file_name + '.tex'
# print_or_not = args.print

# try:
#     file = open('polys_291.txt')
# except FileNotFoundError:
#     print('Incorrect input.')
#     sys.exit()
try:
    with open ('Tests/polys_4.txt') as file:
        Matrix = []
        for line in file:
            line = line.replace(' ','').split()
            if line:
                for i in line:
                    line = list(i)
                    line = [int(x) for x in line]
except ValueError:
    print('Incorrect input.')
    sys.exit()

with open ('Tests/polys_4.txt') as file:
    Matrix = []
    for line in file:
        line = line.replace(' ','').split()
        if line:
            for i in line:
                line = list(i)
                line = [int(x) for x in line]
            Matrix.append(line)

try:
    if not all(x == 0 or x == 1 for m in Matrix for x in m):
        raise ValueError
    if len(set([len(x) for x in Matrix])) != 1 or len(Matrix) <2 or len(Matrix) >50 or len(Matrix[0]) <2 or len(Matrix[0])>50:
        raise ValueError
except ValueError:
    print('Incorrect input.')
    sys.exit()

shapes = []
nb_of_shapes = 1
for i in range(len(Matrix)):
    for j in range(len(Matrix[0])):
        if Matrix[i][j] == 1:
            nb_of_shapes += 1
            neighbour = [[i,j-1],[i,j]]
            for x in range(len(Matrix[0])*len(Matrix)-1):
                if x >len(neighbour)-2:
                    x = len(neighbour)-2
                next_point = find_neighbour_1(neighbour[x], neighbour[x + 1], Matrix)
                if not next_point:
                    print('Cannot get polygons as expected.')
                    sys.exit()
                ##==============Error
#=================================================================
                if next_point != [i,j]:
                    neighbour.append(next_point)
                else:
                    Matrix[i][j] = nb_of_shapes
                    neighbour.pop(0)
                    break
            if neighbour[-1] == neighbour[1]:
                print('Cannot get polygons as expected.')
                sys.exit()
                ##==============Error
#  =================================================================
            for m in range(1, len(neighbour)-1):
                for n in range(len(neighbour)-1,m+2,-1):
                    if neighbour[n] == neighbour[m]:
                        for s in range(m + 1, n+1):
                            neighbour.pop(m + 1)
                        break
            for p in neighbour:
                Matrix[p[0]][p[1]] = nb_of_shapes
            shapes.append(neighbour)
for i in Matrix:
    for j in i:
        if j <10:
            print(j, end='  ')
        else:
            print(j,end = ' ')
    print('')
#===============depth==================
depth = [0]*len(shapes)
for i in shapes:
    for m in range(len(shapes)):
        if shapes[m] != i:
            X = point_in_shape(shapes[m][0],i)
            if X:
                depth[m] += 1
#=============depth========================
shapes_detail = []
for x in range(len(shapes)):
    enter_direction_list = [direction(shapes[x][i - 1], shapes[x][i]) for i in range(len(shapes[x]))]
    inflection_points = [shapes[x][i-1] for i in range(len(shapes[x])) if enter_direction_list[i] != enter_direction_list[i - 1]]
    if inflection_points[0] != shapes[x][0]:
        inflection_points.append(inflection_points[0])
        inflection_points.pop(0)
    Perimeter, area, convex, invariant = shape_analyse(shapes[x])
    shapes_detail.append([inflection_points, Perimeter, area, convex, invariant, depth[x]])

areas = [x[2] for x in shapes_detail]
max_area = round(max(areas),2)
min_area = round(min(areas),2)
for x in shapes_detail:
    if max_area - min_area == 0:
        colour = 0
    else:
        colour = round(round((max_area - x[2]),3)*100/round((max_area - min_area),3))
    x.append(colour)

#if not print_or_not:
count = 0
for i in shapes_detail:
    count += 1
    print('Polygon {}:\n'
          '    Perimeter: {}\n'
          '    Area: {:.2f}\n'
          '    Convex: {}\n'
          '    Nb of invariant rotations: {}\n'
          '    Depth: {}\n'
          '    Colour: {}'.format(count, i[1], i[2], i[3], i[4], i[5], i[-1]))

# else:
#     shapes_detail_ordered = sorted(shapes_detail, key = lambda x : (x[5],x[0][0],x[0][1]))
#     with open(tex_file_name, 'w') as tex_file:
#         print('\\documentclass[10pt]{article}\n'
#               '\\usepackage{tikz}\n'
#               '\\usepackage[margin=0cm]{geometry}\n'
#               '\\pagestyle{empty}\n'
#               '\n'
#               '\\begin{document}\n'
#               '\n'
#               '\\vspace*{\\fill}\n'
#               '\\begin{center}\n'
#               '\\begin{tikzpicture}[x=0.4cm, y=-0.4cm, thick, brown]', file=tex_file)
#         print('\\draw[ultra thick] (0, 0) -- ({}, 0) -- ({}, {}) -- (0, {}) -- cycle;'.format(len(Matrix[0])-1, len(Matrix[0])-1,len(Matrix)-1, len(Matrix)-1), file=tex_file)
#         depth_print = -1
#         for x in shapes_detail_ordered:
#             output_points = [str((i[1], i[0])) for i in x[0]]
#             output_points = ' -- '.join(output_points)
#             if depth_print != x[5]:
#                 depth_print = x[5]
#                 print('%Depth {}'.format(depth_print), file=tex_file)
#             print('\\filldraw[fill=orange!{}!yellow] {} -- cycle;'.format(x[-1],output_points), file=tex_file)
#         print('\\end{tikzpicture}\n'
#               '\\end{center}\n'
#               '\\vspace*{\\fill}\n'
#               '\n'
#               '\\end{document}', file=tex_file)









