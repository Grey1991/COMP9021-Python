L = [10,13,20,30,40,42,44, 46, 48, 50, 60, 70, 80, 82, 85, 87,90, 100, 101, 110, 113, 117, 121]
Lset = set(L)
ride_len = 0
for i in range(0,len(L)-1):
    for n in range(i+1,len(L)):
        diff = L[n] - L[i]
        L2 = range(L[i],L[-1]+1,diff)
        current_len = 0
        for m in range(0,len(L2)):
            if L2[m] in Lset:
                current_len += 1
            else:
                break
        if current_len > ride_len:
            ride_len = current_len
value = len(L) - ride_len
print(value)