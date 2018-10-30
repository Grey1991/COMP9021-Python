

with open ('polys_3.txt') as file:
    Matrix = []
    for line in file:
        line = line.replace(' ','').split()
        if line:
            for i in line:
                line = list(i)
                line = [int(x) for x in line]
            Matrix.append(line)

#for i in Matrix:
#    for j in i:
 #       print(j,end=' ')
 #   print('')

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

def colour_neighbour_1(n,m,L,N):
    enter_direction = direction(n,m)
    neighbour_points = [[m[0]-1,m[1]],[m[0]-1,m[1]+1],[m[0],m[1]+1],[m[0]+1,m[1]+1],[m[0]+1,m[1]],[m[0]+1,m[1]-1],[m[0],m[1]-1],[m[0]-1,m[1]-1]]
    neighbour_1_point = None
    for i in range(2,8):
        x = neighbour_points[(enter_direction+i)%8][0]
        y = neighbour_points[(enter_direction+i)%8][1]
        if 0<= x < len(L) and 0<= y < len(L[0]) and L[x][y] == 1:
            L[x][y] = N
            neighbour_1_point = [x,y]
            break
    return neighbour_1_point

def neighbour_self(n,m,L,N):
    enter_direction = direction(n,m)
    neighbour_points = [[m[0]-1,m[1]],[m[0]-1,m[1]+1],[m[0],m[1]+1],[m[0]+1,m[1]+1],[m[0]+1,m[1]],[m[0]+1,m[1]-1],[m[0],m[1]-1],[m[0]-1,m[1]-1]]
    neighbour_self_point = None
    for i in range(2,8):
        x = neighbour_points[(enter_direction+i)%8][0]
        y = neighbour_points[(enter_direction+i)%8][1]
        if 0<= x < len(L) and 0<= y < len(L[0]) and L[x][y] == N:
            neighbour_self_point = [x,y]
            break
    return neighbour_self_point

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
    in_out_direction = [abs((enter_direction_list[i] + 4) % 8 - enter_direction_list[i - 1]) - 4 for i in
                        range(len(enter_direction_list))]
    inflection_points = [L[x] for x in range(len(in_out_direction)) if in_out_direction[x] != 4]
    if len(inflection_points) %2 != 0:
        invariant = 1
    else:
        middle_x = (inflection_points[0][0] + inflection_points[len(inflection_points)//2][0])/2
        middle_y = (inflection_points[0][1] + inflection_points[len(inflection_points)//2][1])/2
        if all(middle_x == (inflection_points[x][0] + inflection_points[len(inflection_points)//2+x][0])/2 \
                and middle_y == (inflection_points[x][1] + inflection_points[len(inflection_points)//2+x][1])/2 for\
               x in range(len(inflection_points) // 2)):
            if len(inflection_points) %4 ==0 and \
                    all([middle_y-inflection_points[x][1]+middle_x,inflection_points[x][0]-middle_x+middle_y] in inflection_points for x in range(len(inflection_points)//4)):
                invariant = 4
            else:
                invariant = 2
        else:
            invariant = 1
    return Perimeter,area,convex,invariant

def point_in_shape(point,shape):
    count = 0
    enter_direction_list = [direction(shape[i - 1], shape[i]) for i in range(len(shape))]
    in_out_direction = [abs((enter_direction_list[i] + 4) % 8 - enter_direction_list[i - 1]) - 4 for i in
                        range(len(enter_direction_list))]
    inflection_points = [shape[x] for x in range(len(in_out_direction)) if in_out_direction[x] != 4]
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

shapes=[]
nb_of_shapes = 1
for i in range(len(Matrix)):
    for j in range(len(Matrix[0])):
        if Matrix[i][j] == 1:
            nb_of_shapes += 1
            neighbour = [[i,j-1],[i,j]]
            drop_shape = []
            for x in range(len(Matrix[0])*len(Matrix)-1):
                if x >len(neighbour)-2:
                    x = len(neighbour)-2
                next_point = colour_neighbour_1(neighbour[x], neighbour[x + 1], Matrix, nb_of_shapes)
                if not next_point:
                    next_point = neighbour_self(neighbour[x], neighbour[x + 1], Matrix, nb_of_shapes)
                    if not next_point:
                        break
                ##==============Error
#=================================================================
                if next_point != [i,j]:
                    neighbour.append(next_point)
                    if next_point == neighbour[-3]:
                        break
                ##================Error
#=========================================================
                    for m in range(2,len(neighbour)-3):
                        if next_point == neighbour[m]:
                            for s in range(m + 1, len(neighbour)-1):
                                drop_shape.append(neighbour[s])
                                Matrix[neighbour[s][0]][neighbour[s][1]] = -1
                            neighbour = [neighbour[n] for n in range(m+1)]
                            if not colour_neighbour_1(neighbour[-2],neighbour[-1],Matrix,nb_of_shapes):
                                drop_shape.append(neighbour[m])
                                Matrix[neighbour[m][0]][neighbour[m][1]] = -1
                                neighbour.pop()
                            break
                else:
                    Matrix[i][j] = nb_of_shapes
                    neighbour.pop(0)
                    shapes.append(neighbour)
                    break
            if drop_shape:
                for d in drop_shape:
                    Matrix[d[0]][d[1]] = 1
'''for i in Matrix:
    for j in i:
        print(j,end=' ')
    print('')'''
depth = [0]*len(shapes)
for i in shapes:
    for m in range(len(shapes)):
        if shapes[m] != i:
            X = point_in_shape(shapes[m][0],i)
            if X:
                depth[m] += 1
count = 0
for i in range(len(shapes)):
    count +=1
    Perimeter,area,convex,invariant = shape_analyse(shapes[i])
    print('Polygon {}:\n'
          '    Perimeter: {}\n'
          '    Area: {:.2f}\n'
          '    Convex: {}\n'
          '    Nb of invariant rotations: {}\n'
          '    Depth: {}'.format(count,Perimeter,area,convex,invariant,depth[i]))

