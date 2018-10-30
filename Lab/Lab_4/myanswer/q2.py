
def pascal_triangle(N):
    List=[[1],[1,1]]
    if N >= 2:
        for n in range(2,N+1):
            L=[List[n-1][i]+List[n-1][i+1] for i in range(n-1)]
            L.insert(0,1)
            L.append(1)
            List.append(L)
    return List
while True:
    try:
        N = int(input('Enter a nonnegative integer: '))
        if N < 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect input, try again')
List_pascal_triangle = pascal_triangle(N)
width = len(str(List_pascal_triangle[N][N // 2]))
for n in range(N + 1):
    print(' ' * width * (N - n), end = '')
    for k in range(n + 1):
        print('{:{}d}'.format(List_pascal_triangle[n][k], width) + ' ' * width, end = '')
    print()
