def solution(L):
    L_new = [L[len(L)//2]]
    L.pop(len(L)//2)
    while L:
        L_new.append(L[0])
        L.pop(0)
        if L:
            L_new.append(L[-1])
            L.pop()
    return L_new

