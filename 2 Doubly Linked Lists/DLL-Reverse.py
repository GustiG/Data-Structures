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
        

    ## WRITE REVERSE METHOD HERE ##
    #                             #
    #                             #
    #                             #
    #                             #
    ###############################

    def reverse(self):
        if self.length <= 1:
            return
        temp = self.head
        while temp:
            temp.next, temp.prev = temp.prev, temp.next
            temp = temp.prev
        self.head, self.tail = self.tail, self.head

    
        

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)


print('DLL before reverse():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.reverse()


print('\nDLL after reverse():')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before reverse():
    1
    2
    3
    4
    5

    DLL after reverse():
    5
    4
    3
    2
    1

    SOLUTION:

       def reverse(self):
        temp = self.head
        while temp is not None:
            # swap the prev and next pointers of node points to
            temp.prev, temp.next = temp.next, temp.prev
            
            # move to the next node
            temp = temp.prev
            
        # swap the head and tail pointers
        self.head, self.tail = self.tail, self.head


This code is designed to reverse a doubly linked list in-place. 
Here's a step-by-step explanation:

Initialization:

The method starts by assigning the temp variable to the head 
of the list. This variable will be used to traverse the list 
from the beginning to the end.

Traversal and Swapping Pointers:

The code enters a while loop that continues as long as temp 
is not None. This condition ensures that the loop goes through 
every node in the list.

Inside the loop, for each node that temp points to, the prev 
and next pointers are swapped. This operation reverses the 
direction of the links for each node.

temp.prev, temp.next = temp.next, temp.prev effectively changes 
the direction of the pointers. For example, if a node N points 
forward to N+1 (next) and backward to N-1 (prev), after this line, 
it will point forward to N-1 and backward to N+1.

After swapping the pointers of the current node, temp is updated 
to temp.prev, which, due to the swap, now points to the next node 
in the original sequence. This update moves the traversal forward 
through the list, even though it seemingly moves to the prev node 
due to the reversed pointers.

Final Adjustment:

After the loop completes, meaning temp has reached beyond the 
end of the list (temp is None), the head and tail of the list 
are swapped.

This swapping of self.head and self.tail is necessary because, 
by reversing the direction of each node's pointers, what was 
originally the head of the list (the starting point) is now at 
the end position, and what was the tail (the end point) is now 
at the start. Swapping these pointers ensures that the list's 
head and tail properties correctly represent the new start and 
end of the reversed list.

In summary, this code methodically reverses the direction of a 
doubly linked list by swapping the forward and backward pointers 
of each node and then adjusting the head and tail pointers of the 
list to reflect the reversed order.



Here's the breakdown step-by-step:



def reverse(self):

This line starts the definition of a method named reverse. It
's designed to reverse a doubly linked list.

temp = self.head

Here, we initialize temp with the first node of the list, 
referred to as the head. temp will be used to traverse the list.

while temp is not None:

This loop continues as long as temp is pointing to a node. 
It ensures every node in the list is visited.

temp.prev, temp.next = temp.next, temp.prev

Within each iteration, the current node's pointers to the 
previous and next nodes are swapped. This action reverses the 
direction of links for the node temp is currently on.

temp = temp.prev

After swapping the pointers, temp is moved to the next node in 
the original order, which is now accessible via temp.prev due to 
the swap. This step advances the traversal.

self.head, self.tail = self.tail, self.head

Once all nodes have been processed and the loop exits, the list's 
head and tail pointers are swapped. This final step adjusts the 
list's endpoints to reflect the reversed order correctly.



Code with inline comments:



def reverse(self):
    # Initialize 'temp' to point to the list's head.
    # 'temp' is used to traverse the list.
    temp = self.head
    
    # Loop until 'temp' is None, signifying the
    # end of the list has been reached.
    while temp is not None:
        # Swap the current node's 'prev' and 'next'.
        # This reverses the link direction for the node.
        # 'prev' becomes 'next', and vice versa.
        temp.prev, temp.next = temp.next, temp.prev
        
        # Move to the next node in the original list
        # order to continue the reversal.
        # After swapping, 'prev' points to the next
        # node in original order, so move to 'temp.prev'.
        temp = temp.prev
        
    # After reversing all nodes, update the list's
    # head and tail to reflect the new order.
    # The original head is now the tail, and the
    # original tail is now the head.
    self.head, self.tail = self.tail, self.head

"""

