
from linked_list import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def remove_duplicates(self):
        '''
        >>> LL = ExtendedLinkedList()
        >>> LL.remove_duplicates()
        >>> LL.print()
        >>> LL = ExtendedLinkedList([1])
        >>> LL.remove_duplicates()
        >>> LL.print()
        1
        >>> LL = ExtendedLinkedList([1, 1])
        >>> LL.remove_duplicates()
        >>> LL.print()
        1
        >>> LL = ExtendedLinkedList([1, 1, 1])
        >>> LL.remove_duplicates()
        >>> LL.print()
        1
        >>> LL = ExtendedLinkedList([1, 1, 1, 2, 2, 2])
        >>> LL.remove_duplicates()
        >>> LL.print()
        1, 2
        >>> LL = ExtendedLinkedList([1, 2, 1, 2, 1, 2])
        >>> LL.remove_duplicates()
        >>> LL.print()
        1, 2
        >>> LL = ExtendedLinkedList([1, 2, 3])
        >>> LL.remove_duplicates()
        >>> LL.print()
        1, 2, 3
        >>> LL = ExtendedLinkedList([1, 1, 1, 2, 1, 2, 1, 2, 3, 3, 2, 1])
        >>> LL.remove_duplicates()
        >>> LL.print()
        1, 2, 3
        '''
        self.reverse()
        if self.head:
            S = {self.head.value}
            node = self.head.next_node
            while node:
                if node.value in S:
                    self.delete_value(node.value)
                else:
                    S.add(node.value)
                node = node.next_node
        self.reverse()
            
        
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #LL = ExtendedLinkedList([1, 1, 1, 2, 1, 2, 1, 2, 3, 3, 2, 1])
    #LL.remove_duplicates()
    #LL.print()
    

    
