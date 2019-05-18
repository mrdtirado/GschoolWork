class Node(object):
    '''
    Node Class for Linked Lists
    '''
    def __init__(self, data, next_node=None):
        '''
        Instantiate the value and next node attribute of the class
        '''
        self.value = data
        self.next_node = next_node

    def set_value(self):
        '''
        Method to set the value of the node
        Sets the value at a specific node
        '''
        return self.value

    def set_next(self, new_next):
        '''
        Method to set the pointer to the next value
        Sets up the pointer to the next node
        '''
        self.next_node = new_next


    def value(self):
        '''
        Return the value stored in the node
        returns the value in the Node
        '''
        return self.value

    def next(self):
        '''
        Return the next Node in the list
        Goes to the next value in the linked list as specificed by set_next
        '''
        return self.next_node
