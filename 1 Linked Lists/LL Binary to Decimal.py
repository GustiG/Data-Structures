'''
Your task is to implement the binary_to_decimal method for 
the LinkedList class. This method should convert a binary number, 
represented as a linked list, to its decimal equivalent.

In this context, a binary number is a sequence of 0s and 1s. 
The LinkedList class represents this binary number such that 
each node in the linked list contains a single digit (0 or 1) 
of the binary number, and the whole number is formed by traversing 
the linked list from the head to the end.

The binary_to_decimal method should start from the head of the 
linked list and use each node's value to calculate the corresponding 
decimal number. The formula to convert a binary number to decimal is 
as follows:

To put it in simple terms, each digit of the binary number is 
multiplied by 2 raised to the power equivalent to the position of 
the digit, counting from right to left starting from 0, 
and all the results are summed together to get the decimal number.

The binary_to_decimal method should return this calculated 
decimal number.



Examples

Consider the binary number 101. If this number is represented as 
a linked list, the head of the linked list will contain the digit 1, 
the next node will contain 0, and the last node will contain 1. 
When we apply the binary_to_decimal method on this linked list, 
the method should return the number 5, which is the decimal equivalent 
of binary 101.

Similarly, for a linked list representing the binary number 1101, 
the binary_to_decimal method should return the number 13.

Here's how you can create these linked lists and call the 
binary_to_decimal method:

# Create a linked list for binary number 101
linked_list = LinkedList(1)
linked_list.append(0)
linked_list.append(1)
 
# Convert binary to decimal
print(linked_list.binary_to_decimal())  # Output: 5
 
# Create a linked list for binary number 1101
linked_list = LinkedList(1)
linked_list.append(1)
linked_list.append(0)
linked_list.append(1)
 
# Convert binary to decimal
print(linked_list.binary_to_decimal())  # Output: 13

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values)) 

    # WRITE BINARY_TO_DECIMAL METHOD HERE #
    #                                     #
    #                                     #
    #                                     #
    #                                     #
    #######################################

    def binary_to_decimal(self):
        num = 0
        cur = self.head
        while cur:
            num = num * 2 + cur.value
            cur = cur.next
        return num
    
      
  
# Test case 1: Binary number 110 = Decimal number 6
linked_list = LinkedList(1)
linked_list.append(1)
linked_list.append(0)
result = linked_list.binary_to_decimal()
try:
    assert result == 6
    print("Test case 1 passed, returned: ", result)
except AssertionError:
    print("Test case 1 failed, returned: ", result)

# Test case 2: Binary number 1000 = Decimal number 8
linked_list = LinkedList(1)
linked_list.append(0)
linked_list.append(0)
linked_list.append(0)
result = linked_list.binary_to_decimal()
try:
    assert result == 8
    print("Test case 2 passed, returned: ", result)
except AssertionError:
    print("Test case 2 failed, returned: ", result)

# Test case 3: Binary number 0 = Decimal number 0
linked_list = LinkedList(0)
result = linked_list.binary_to_decimal()
try:
    assert result == 0
    print("Test case 3 passed, returned: ", result)
except AssertionError:
    print("Test case 3 failed, returned: ", result)

# Test case 4: Binary number 1 = Decimal number 1
linked_list = LinkedList(1)
result = linked_list.binary_to_decimal()
try:
    assert result == 1
    print("Test case 4 passed, returned: ", result)
except AssertionError:
    print("Test case 4 failed, returned: ", result)

# Test case 5: Binary number 1101 = Decimal number 13
linked_list = LinkedList(1)
linked_list.append(1)
linked_list.append(0)
linked_list.append(1)
result = linked_list.binary_to_decimal()
try:
    assert result == 13
    print("Test case 5 passed, returned: ", result)
except AssertionError:
    print("Test case 5 failed, returned: ", result)
    
 
"""
    EXPECTED OUTPUT:
    ----------------
    Test case 1 passed, returned:  6
    Test case 2 passed, returned:  8
    Test case 3 passed, returned:  0
    Test case 4 passed, returned:  1
    Test case 5 passed, returned:  13
"""

'''
  def binary_to_decimal(self):
        num = 0
        current = self.head
        while current:
            num = num * 2 + current.value
            current = current.next
        return num






Given the linked list: 1 → 0 → 1 → 0

This represents the binary number 1010, 
where the head of the list is the most significant bit 
(MSB) and the tail is the least significant bit (LSB).

Method Walkthrough:

def binary_to_decimal(self):


Initialize the decimal number:

num = 0
Here, num will store our resulting decimal number. 
We initialize it to 0.



Start at the head of the linked list:

current = self.head
This current pointer will help us traverse the linked list 
from the start (MSB) to the end (LSB).



Traverse the linked list:

while current:
This loop runs as long as we have nodes left in the linked list.



Convert the binary number to decimal:

    num = num * 2 + current.value


For every node we encounter, we:

Multiply the current num by 2. This shifts our binary number left, 
preparing it for the next bit. It's analogous to multiplying by 10 
in decimal arithmetic.

Add the value of the current node (0 or 1) to num.



Illustrative Steps for 1010:

Starting with num as 0.

First node (MSB) is 1. So, num = 0 * 2 + 1 which makes num equal to 1

Move to the next node, which is 0. 
Now, num = 1 * 2 + 0 which makes num equal to 2.

The next node is 1. So, num = 2 * 2 + 1 which results in num 
becoming 5.

The last node (LSB) is 0. Thus, num = 5 * 2 + 0 which makes num 
equal to 10.

Consequently, the binary number 1010 converts to the decimal 
number 10.



Proceed to the next node:

    current = current.next
This line shifts our attention to the next node in the linked list.



Return the decimal number:

return num
After processing all the bits in our binary number 
(i.e., all the nodes in our linked list), we can return our 
decimal result stored in num.


Conclusion:

The process for converting binary to decimal using a linked list 
reflects standard binary conversion rules. 
We work from the MSB (head of the linked list) to the LSB (tail), 
doubling our current result and adding the next bit at every step. 
This method ensures that each binary bit contributes the correct 
power of 2 to our final decimal result. 
In our example, 1010 rightly converts to 10.





Code with inline comments:



def binary_to_decimal(self):
    # 1. Initialize a variable 'num' to 0. 
    # This will be used to accumulate the 
    # decimal value as we traverse the linked list.
    num = 0
    
    # 2. Start at the head of the linked list.
    current = self.head
 
    # 3. Traverse through the linked list.
    while current:
        # 3.1. For each node, left shift the accumulated value 
        # by 1 position. 
        # This is the same as multiplying by 2. 
        # This step ensures that we are 
        # moving to the next binary position.
        # 
        # Example: If num is '10' (binary for 2) and next 
        # node value is '1', 
        # left shifting '10' results in '100' (binary for 4). 
        # Now, adding the next node value gives '101' (binary for 5).
        num = num * 2
        
        # 3.2. Add the current node's value 
        # (which should be either 0 or 1) 
        # to the accumulated value 'num'.
        num = num + current.value
        
        # OR both the above steps can be combined as:
        # num = num * 2 + current.value
        
        # 3.3. Move to the next node in the list.
        current = current.next
 
    # 4. Return the accumulated decimal value.
    return num

'''