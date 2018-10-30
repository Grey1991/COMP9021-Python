# Finds all triples of positive integers (i, j, k) such that
# i, j and k are two digit numbers, i < j < k,
# every digit occurs at most once in i, j and k,
# and the product of i, j and k is a 6-digit number
# consisting precisely of the digits that occur in i, j and k.


# If i, j and k are numbers in the range [10, 99], i < j < k,
# and every digit occurs at most once in i, j and k
# then 10 <= i <= 76, j <= 87, and k <= 98. 
min_i = 10
max_i = 76
max_j = 87
max_k = 98

for i in range(min_i, max_i + 1):
    i_digits = {i // 10, i % 10}
    if len(i_digits) != 2:
        continue
    # Insert your code here to generate j and k,
    # check that they satisfy the desired conditions,
    # and check that i * j * k also satisfies the desired condition,
    # in which base one solution is ouput.
    min_j = (i//10)*10
    for j in range(min_j, max_j+1):
        j_digits = {j//10,j%10}
        s_ij = j_digits | i_digits
        if len(s_ij) != 4:
            continue
        min_k = (j//10)*10
        for k in range(min_k,max_k+1):
            k_digits = {k//10,k%10}
            s_ijk = k_digits|s_ij
            if len(s_ijk) != 6:
                continue
            n = i*j*k
            if n <100000:
                continue
            m = str(n)
            s_m = {int(m[x]) for x in range(6)}
            if len(s_m)==6 and len(s_m & s_ijk)==6:
                print('{} x {} x {} = {} is a solution.'.format(i,j,k,n))
            
