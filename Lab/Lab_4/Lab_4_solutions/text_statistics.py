# Prompts the user for the name of a file and outputs
# how many occurrences of each digit has been input, if any.
#
# Written by Eric Martin for COMP9021


with open(input('Enter the name of a file: ')) as file:
    digit_found = False
    count = [0] * 10
    for line in file:
        for c in line:
            if c.isdigit():
                digit_found = True
                count[ord(c) - ord('0')] += 1
    if not digit_found:
        print('There is no digit in this file.')
    else:
        print('Digits: ', end = '')
        for i in range(10):
            if count[i]:
                print(f'{i:4d}', end = '')
        print('\nCount:  ', end = '')
        for i in range(10):
            if count[i]:
                print(f'{count[i]:4d}', end = '')
        print()


          
        
