class Stack:

    '''
    >>> s = Stack()
    >>> print s.isEmpty()
    True
    >>> s.push(4)
    >>> s.push(5)
    >>> s.peek()
    5
    >>> s.size()
    2
    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

