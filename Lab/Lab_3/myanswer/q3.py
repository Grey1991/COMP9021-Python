# Finds all triples of consecutive positive three-digit integers
# each of which is the sum of two squares.

L=[]
for a in range(31,-1,-1):
    for b in range(31,a-1,-1):
        m = a**2 +b**2
        if m >= 100 and m< 1000:
            List_m = [m,a,b]
            if all(L[x][0]!=m for x in range(len(L))) or len(L)==0:
                L.append(List_m)
L.sort()
for i in range(len(L)-2):
    if L[i][0]+2 == L[i+1][0]+1 == L[i+2][0]:
        print('({}, {}, {}) (equal to ({}^2+{}^2, {}^2+{}^2, {}^2+{}^2)) is a solution.'.format(L[i][0],L[i+1][0],L[i+2][0],L[i][1],L[i][2],L[i+1][1],L[i+1][2],L[i+2][1],L[i+2][2]))
