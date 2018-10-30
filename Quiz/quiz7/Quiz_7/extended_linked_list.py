# Written by **** for COMP9021

from linked_list import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        # Replace pass above with your code
        node = self.head
        self.min = self.head
        while node and node.next_node:
            if self.min.value > node.next_node.value:
                self.min = node.next_node
                last_of_min_node = node
            node = node.next_node
        if self.min == self.head:
            node = self.head
            while node.next_node:
                last_node = node
                node = node.next_node
            node.next_node = self.head
            self.head = node
            last_node.next_node = None
        else:
            orgin_head = self.head
            self.head = last_of_min_node
            node = self.head
            while node.next_node:
                node = node.next_node
            node.next_node = orgin_head
            node = orgin_head
            while node.next_node != self.head:
                node = node.next_node
            node.next_node = None
        node = self.head
        self.head = node.next_node
        for i in range(len(self)//2+1):
            if node.next_node.next_node:
                temp = node.next_node.next_node
                node.next_node.next_node = node
                node.next_node = temp.next_node
                node = temp
            else:
                node.next_node.next_node = node
                node.next_node = None





    
    
    
