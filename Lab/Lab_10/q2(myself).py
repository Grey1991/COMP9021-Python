def all_possible(L):    
    if len(L) == 1:
        return [str(L[0])]
    return ['('+a+' - '+b+')' for i in range(1,len(L))
                                for a in all_possible(L[:i])
                                    for b in all_possible(L[i:])]

def subtractions(L,N):
    for i in all_possible(L):
        if eval(i) == N:
            print(i[1:-1])
