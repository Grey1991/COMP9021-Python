# Written by *** for COMP9021


from binary_tree import *
from math import log


class PriorityQueue(BinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        if self.size() == 0:
            self.value = value
            self.left_node = PriorityQueue()
            self.right_node = PriorityQueue()
        else:
            L = [self]
            for i in L:
                if i.left_node:
                    L.append(i.left_node)
                if i.right_node:
                    L.append(i.right_node)
            L_value = [i.value for i in L if i.value is not None]
            L_value.append(value)
            a = len(L_value) -1
            while a > 0:
                if L_value[a] < L_value[int((a+1)/2)-1]:
                    L_value[a],L_value[int((a+1)/2)-1] = L_value[int((a+1)/2)-1],L_value[a]
                a = int((a+1)/2)-1
            new_tree = [self]
            for i in new_tree:
                if L_value:
                    i.value = L_value[0]
                    i.left_node = PriorityQueue()
                    i.right_node = PriorityQueue()
                    new_tree.append(i.left_node)
                    new_tree.append(i.right_node)
                    L_value.pop(0)
