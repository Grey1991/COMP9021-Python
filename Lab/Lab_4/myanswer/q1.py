# Prompts the user for a strictly positive number N
# and outputs an equilateral triangle of height N.
# The top of the triangle (line 1) is labeled with the letter A.
# For all nonzero p < N, line p+1 of the triangle is labeled
# with letters that go up in alphabetical order modulo 26
# from the beginning of the line to the middle of the line,
# starting wth the letter that comes next in alphabetical order
# modulo 26 to the letter in the middle of line p,
# and then down in alphabetical order modulo 26
# from the middle of the line to the end of the line.


while True:
    try:
        height = int(input('Enter strictly positive number: '))
        if height <= 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect input, try again.')

A_code = ord('A')
c = A_code

for i in range(1, height + 1):

    b = ((i-1)*i//2)%26 + A_code
    print(' '*(height-i),end='')
    for j in range(0,i):
        print(chr(((i-1)*i//2+j)%26+65),end='')
    if i >=2:
        for n in range(i-2,-1,-1):
            print(chr(((i-1)*i//2+n)%26+65),end='')
    print('')
        
    
