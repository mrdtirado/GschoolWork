class LinkedList(object):
    '''
    A Linked List Class
    '''
    def __init__(self):
        '''
        Takes a python list and transforms to a linked list, should have a head attribute that is the first node in the linked list
        Input: python list
        Output: None
        '''
        self.start_node = None



    def append(self, data):
        '''
        Takes a  value and adds it in a new Node to the end of the list
        Input: value to store
        Output: None
        '''
        new_node = Node(data)
        print(new_node.value)
        if self.start_node is None:
            self.start_node = new_node
            print(self.start_node.value)
            return
        n = self.start_node
        while n.next_node is not None:
            n = n.next_node
            print(n.value)
        n.next_node = new_node



    def copy(self):
        '''
        Returns a copy of the link list
        Think about mutability and what you are trying to do
        '''

        pass

    def count(self):
        '''
        Returns the number of items in the list
        Think about the time complexity
        '''
        pass

    def extend(self):
        '''
        Extend the linked list
        Input: Linked List
        Output: None
        '''
        pass

    def index(self):
        '''
        Find the index at which a passed value exist. Return -1 if value not in list
        Input: value to find
        Return: Int: node number of first existance
                Int: -1 if value not in linked list
        ex:
        >>> ll = LinkedList([2, 4, 7, 4])
        >>> ll.index(4)
        1
        '''

        pass

    def insert(self):
        '''
        Insert a new Node object into the list at the given index
        Input:  Value to add
                Index to add value
        Output: None
        '''
        pass

    def pop(self):
        '''
        Remove and return last value in the linked list
        Input: None
        Output: Value of node
        '''
        pass

    def reverse(self):
        '''
        Return a linked list in reverse order
        Input: None
        Output: Linked List
        '''
        pass

    def sort(self):
        '''
        Sort the linked list
        Input: None
        Output: None
        '''
pass
