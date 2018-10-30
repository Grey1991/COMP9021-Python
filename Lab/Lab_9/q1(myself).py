# Uses the Stack interface to evaluate an arithmetic expression
# written in postfix and built from natural numbers using
# the binary +, -, * and / operators.             
#
# Written by Eric Martin for COMP9021


import re
from operator import add, sub, mul, truediv

from array_stack import ArrayStack, EmptyStackError


def evaluate(expression):
   '''
    Checks whether an expression is a valid fully parentherised infix expression,
    and in case the answer is yes, returns the value of the expression,
    provided that no division by 0 is attempted; otherwise, return None.

    >>> evaluate('100')
    100
    >>> evaluate('[(1 - 20) + 300]')
    281
    >>> evaluate('[1 - {20 + 300}]')
    -319
    >>> evaluate('( { 20*4 }/5 )')
    16.0
    >>> evaluate('(20*[4/5])')
    16.0
    >>> evaluate('({1 + (20 * 30)} - [400 / 500])')
    600.2
    >>> evaluate('{1 + [((20*30)-400) / 500]}')
    1.4
    >>> evaluate('[1 + {(2 * (3+{4*5})) / ([6*7]-[8/9]) }]')
    2.1189189189189186
    >>> evaluate('100 + 3')
    >>> evaluate('(100 + 3')
    >>> evaluate('(100 + -3)')
    >>> evaluate('(100 \ 50)')
    >>> evaluate('(100 / 0)')    
    '''
   if any(not (c.isdigit() or c.isspace() or c in '+-*/(){}[]') for c in expression):
      return
    # Tokens can be natural numbers, +, -, *, and /
   tokens = re.compile('(\d+|\+|-|\*|/|\[|\]|\(|\)|{|})').findall(expression)
   try:
      value = evaluate_expression(tokens)
      return value
   except ZeroDivisionError:
      return


def evaluate_expression(tokens):
   stack = ArrayStack()
   for token in tokens:
      stack.push(token)
      if token in [')','}',']']:
         try:
            right = stack.pop()
            arg_2 = stack.pop()
            if type(arg_2)==str:
               arg_2 = int(arg_2)
            operate = stack.pop()
            arg_1 = stack.pop()
            if type(arg_1)==str:
               arg_1 = int(arg_1)
            left = stack.pop()
         except EmptyStackError:
            return
         except ValueError:
            return
         #print((left,right))
         if (left,right) not in [('(',')'),('{','}'),('[',']')]:
            return
         A ={'+': add, '-': sub, '*': mul, '/': truediv}[operate](arg_1, arg_2)
         #print(A)
         stack.push({'+': add, '-': sub, '*': mul, '/': truediv}[operate](arg_1, arg_2))
         
   if stack.is_empty():
      return
   value = stack.pop()
   if not stack.is_empty():
      return
   if type(value) == str:
      value = int(value)
   return value


if __name__ == '__main__':
   import doctest
   doctest.testmod()

