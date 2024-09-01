class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    # WRITE IS_PALINDROME METHOD HERE #
    #                                 #
    #                                 #
    #                                 #
    #                                 #
    ###################################
    
    def is_palindrome(self):
        if self.length <= 1:
            return True
        forwardNode = self.head
        backwardNode = self.tail

        for _ in range(self.length // 2):
            if forwardNode.value != backwardNode.value:
                return False
            forwardNode = forwardNode.next
            backwardNode = backwardNode.prev
        return True





my_dll_1 = DoublyLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(3)
my_dll_1.append(2)
my_dll_1.append(1)

print('my_dll_1 is_palindrome:')
print( my_dll_1.is_palindrome() )


my_dll_2 = DoublyLinkedList(1)
my_dll_2.append(2)
my_dll_2.append(3)

print('\nmy_dll_2 is_palindrome:')
print( my_dll_2.is_palindrome() )



"""
    EXPECTED OUTPUT:
    ----------------
    my_dll_1 is_palindrome:
    True

    my_dll_2 is_palindrome:
    False

    SOLUTION:

    def is_palindrome(self):
        if self.length <= 1:
            return True
        forward_node = self.head
        backward_node = self.tail
        for i in range(self.length // 2):
            if forward_node.value != backward_node.value:
                return False
            forward_node = forward_node.next
            backward_node = backward_node.prev
        return True


The is_palindrome method in a doubly linked list checks whether 
the list is a palindrome, meaning that it reads the same forwards 
and backwards.

Here's how the method works:

If the length of the list is less than or equal to 1, 
then the list is a palindrome by definition, so the method 
returns True.

The method initializes two pointers, forward_node and backward_node, 
that point to the head and tail of the list, respectively. 
The method then iterates over half of the list, comparing the 
values of the nodes at each end of the list to see if they are 
the same.

If the values of the nodes do not match, the method returns False, 
indicating that the list is not a palindrome. If all of the values 
match, the method returns True, indicating that the list is a 
palindrome.


This implementation of the method takes advantage of the fact that 
a doubly linked list allows for efficient traversal from both ends 
of the list, which makes it possible to check if the list is a 
palindrome in O(n) time, where n is the length of the list.





Code with inline comments:



def is_palindrome(self):
    # 1. If the length of the doubly linked list is 0 or 1, then 
    # the list is trivially a palindrome. 
    if self.length <= 1:
        return True
    
    # 2. Initialize two pointers: 'forward_node' starting at the head 
    # and 'backward_node' starting at the tail.
    forward_node = self.head
    backward_node = self.tail
    
    # 3. Traverse through the first half of the list. We only need to 
    # check half because we're comparing two nodes at once: one from 
    # the beginning and one from the end.
    for i in range(self.length // 2):
        # 3.1. Compare the values of 'forward_node' and 
        # 'backward_node'. 
        # If they're different, the list is not a palindrome.
        if forward_node.value != backward_node.value:
            return False
        
        # 3.2. Move the 'forward_node' one step towards the tail and 
        # the 'backward_node' one step towards the head for the 
        # next iteration.
        forward_node = forward_node.next
        backward_node = backward_node.prev
 
    # 4. If we've gone through the first half of the list without 
    # finding any non-matching node values, 
    # then the list is a palindrome.
    return True

"""

