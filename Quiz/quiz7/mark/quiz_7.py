# Generates a linked list of an even length of 4 or more, determined by user input,
# and reorders the list so that it starts with the first occurrence
# of the smallest element and repeatively moves backwards by one step and forward
# by three steps, wrapping around when needed.

import sys
from random import seed, randrange
from linked_list import *
from extended_linked_list import ExtendedLinkedList

def collect_references(L, length):
    node = L.head
    references = set()
    for i in range(length):
        references.add(id(node))
        node = node.next_node
    return references

provided_input = input('Enter 2 integers: ')
provided_input = provided_input.split()
if len(provided_input) != 2:
    print('Incorrect input, giving up.')
    sys.exit()
seed(int(provided_input[0]))
# An even number at least equal to 4
length = (abs(int(provided_input[1])) + 2) * 2

L = [0] * length
for i in range(length):
    L[i] = randrange(100)

LL = ExtendedLinkedList(L)
LL.print()
references = collect_references(LL, length)
LL.rearrange()
if collect_references(LL, length) != references:
    print('You cheated!')
    sys.exit()
else:
    LL.print()    

