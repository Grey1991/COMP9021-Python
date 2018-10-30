# Written by Eric Martin for COMP9021


'''
A class to manipulate the encoding of a set of (distinct) nonnegative integers {n_1, ..., n_k}
as 2^{n_1} + ... + 2^{n_k}.
A function to create such an object from such a set.
'''


class BitSet:
    def __init__(self, code):
        self.code = code
        self.encoded_set = self._decode()

    def _decode(self):
        return [i for i in range(self.code.bit_length()) if 2 ** i & self.code]
               
    def __repr__(self):
        '''
        >>> BitSet(0)
        BitSet(0)
        >>> BitSet(76)
        BitSet(76)
        '''
        return f'BitSet({self.code})'

    def __str__(self):
        '''
        To display the members of the encoded set,
        from smallest to largest element, in increasing order.
        
        >>> print(BitSet(0))
        {}
        >>> print(BitSet(1))
        {0}
        >>> print(BitSet(3))
        {0, 1}
        >>> print(BitSet(76))
        {2, 3, 6}
        '''
        if self.code == 0:
            return '{}'
        notation = ['{']
        for e in self.encoded_set[: -1]:
            notation.append(f'{e}, ')
        notation.extend((str(self.encoded_set[-1]), '}'))
        return ''.join(notation)

    def __len__(self):
        '''
        Returns the number of elements in the encoded set
        encoding as the argument.
        
        >>> len(BitSet(0))
        0
        >>> len(BitSet(1))
        1
        >>> len(BitSet(76))
        3
        '''
        return len(self.encoded_set)

    def __contains__(self, nonnegative_integer):
        '''
        Returns True or False depending on whether the argument
        belongs to the encoded set.
        
        >>> 0 in BitSet(0)
        False
        >>> 0 in BitSet(1)
        True
        >>> 3 in BitSet(76)
        True
        >>> 4 in BitSet(76)
        False
        '''
        return nonnegative_integer in self.encoded_set

    
def encode_to_bit_set(set_of_nonnegative_integers):
    '''
    Encodes a set and returns the encoding BitSet.
    Here an empty set of curly braces provided as argument
    denotes the empty set, not the empty dictionary.
    
    >>> encode_to_bit_set({})
    BitSet(0)
    >>> encode_to_bit_set({0})
    BitSet(1)
    >>> encode_to_bit_set({0, 1})
    BitSet(3)
    >>> encode_to_bit_set({2, 3, 6})
    BitSet(76)
    '''
    return BitSet(sum(2 ** i for i in set_of_nonnegative_integers))




if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
