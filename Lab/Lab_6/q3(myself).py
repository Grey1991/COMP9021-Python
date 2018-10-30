# Prompts the user for a string w of lowercase letters and outputs the
# longest sequence of consecutive letters that occur in w,
# but with possibly other letters in between, starting as close
# as possible to the beginning of w.
#
# Written by Eric Martin for COMP9021


import sys


word = input('Please input a string of lowercase letters: ')
if not all(c.islower() for c in word):
    print('Incorrect input.')
    sys.exit()
def solution(word):
    L = list(word)
    if len(L) == 1:
        return word
    solution = ''
    for i in range(len(L)-1):
        current = ord(L[i])
        current_string = L[i]
        for j in range(i+1,len(L)):
            if ord(L[j]) == current+1:
                current += 1
                current_string += L[j]
        if len(current_string) > len(solution):
            solution = current_string
    return solution
            
string = solution(word)
print('The solution is: {}'.format(string))
