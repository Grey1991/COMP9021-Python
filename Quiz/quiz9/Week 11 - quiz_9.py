# Prompts the user for a string, checks that it is a corect postfix expression
# built from positive numbers, + and spaces, and if it is,
# outputs a tree representation of the corresponding infix expression.

# Written by *** and Eric Martin for COMP9021


import sys
import re

from array_stack import *
from binary_tree import *


def store_in_two_stacks(expression):
    expression = expression.replace('+',' + ').strip()
    L = re.split(r'\s+',expression)
    for i in L:
        if not re.match(r'^(0|[1-9]+[0-9]*|\+)$',i):
            L = []
    stack_1 = ArrayStack()
    stack_2 = ArrayStack()
    for x in L:
        stack_1.push(x)
        stack_2.push(x)
    return stack_1, stack_2

def stores_correct_postfix_expression(stack):
    num = 1
    while stack:
        e = stack.pop()
        if e == '+':
            num += 1
        if re.match(r'^(0|[1-9]+[0-9]*)$',e):
            num -= 1
        if num < 0:
            return False
    if num != 0:
        return False
    else:
        return True

def transfer_from_stack_to_tree(stack):
    def bulit_tree(node,stack):
        if node.value == '+':
            if stack:
                node.left_node = BinaryTree(stack.pop())
                bulit_tree(node.left_node,stack)
            if stack:
                node.right_node = BinaryTree(stack.pop())
                bulit_tree(node.right_node,stack)
    node_value = stack.pop()
    node = BinaryTree(node_value)
    bulit_tree(node,stack)
    return node
# Possibly define other functions

expression = input('Input an expression: ')
if not expression or expression.isspace():
    sys.exit()
stack_1, stack_2 = store_in_two_stacks(expression)
if not stack_1:
    print('Expression not built from nonnegative numbers and +')
else:
    if not stores_correct_postfix_expression(stack_1):
        print('Not a correct postfix expression')
    else:
        tree = transfer_from_stack_to_tree(stack_2)
        tree.print_binary_tree()
        
