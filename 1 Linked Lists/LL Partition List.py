'''
⚠️ CAUTION: Advanced Challenge Ahead!

This Linked List problem is significantly more challenging than 
the ones we've tackled so far. It's common for students at this 
stage to find this exercise demanding, so don't worry if you're not 
ready to tackle it yet. It's perfectly okay to set it aside and 
revisit it later when you feel more confident.

If you decide to take on this challenge, I strongly advise using 
a hands-on approach: 
grab a piece of paper and visually map out each step.

This problem requires a clear understanding of how elements 
in a Linked List interact and move. 
By now, you've observed numerous Linked List animations 
in the course, which have prepared you for this moment.

This exercise will be a true test of your ability to apply 
those concepts practically. Remember, patience and persistence 
are key here!

Now, here is the exercise:

___________________________________



Implement the partition_list member function for the LinkedList 
class, which partitions the list such that all nodes with values 
less than x come before nodes with values greater than or equal to x.

Note:  This linked list class does NOT have a tail which will make 
this method easier to implement.

The original relative order of the nodes should be preserved.



Details:

The function partition_list takes an integer x as a parameter and 
modifies the current linked list in place according to the specified 
criteria. If the linked list is empty (i.e., head is null), 
the function should return immediately without making any changes.



Example 1:

Input:

Linked List: 3 -> 8 -> 5 -> 10 -> 2 -> 1 x: 5

Process:

Values less than 5: 3, 2, 1

Values greater than or equal to 5: 8, 5, 10

Output:

Linked List: 3 -> 2 -> 1 -> 8 -> 5 -> 10





Example 2:
Input:

Linked List: 1 -> 4 -> 3 -> 2 -> 5 -> 2 x: 3

Process:

Values less than 3: 1, 2, 2

Values greater than or equal to 3: 4, 3, 5

Output:

Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5





Tips:

While traversing the linked list, maintain two separate chains: 
one for values less than x 
and one for values greater than or equal to x.

Use dummy nodes to simplify the handling 
of the heads of these chains.

After processing the entire list, connect the two chains to get 
the desired arrangement.



Note:

The solution must maintain the relative order of nodes. 
For instance, in the first example, even though 8 appears 
before 5 in the original list, the partitioned list must still have 
8 before 5 as their relative order remains unchanged.

Note:

You must solve the problem WITHOUT MODIFYING THE VALUES 
in the list's nodes 
(i.e., only the nodes' next pointers may be changed.)
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
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
#   +===================================================+
#   |               WRITE YOUR CODE HERE                |
#   | Description:                                      |
#   | - This method partitions a linked list around a   |
#   |   value `x`.                                      |
#   | - It rearranges the nodes so that all nodes less  |
#   |   than `x` come before all nodes greater or equal |
#   |   to `x`.                                         |
#   |                                                   |
#   | Tips:                                             |
#   | - We use two dummy nodes, `dummy1` and `dummy2`,  |
#   |   to build two separate lists: one for elements   |
#   |   smaller than `x` and one for elements greater   |
#   |   or equal to `x`.                                |
#   | - `prev1` and `prev2` help us keep track of the   |
#   |   last nodes in these lists.                      |
#   | - Finally, we merge these two lists by setting    |
#   |   `prev1.next = dummy2.next`.                     |
#   | - The head of the resulting list becomes          |
#   |   `dummy1.next`.                                  |
#   +===================================================+

    def partition_list(self, x):
        dummy1  = Node(0)
        dummy2  = Node(0)
        prev1   = dummy1
        prev2   = dummy2
        current = self.head
        for _ in range(self.length):
            if current.value < x:
                prev1.next = current
                prev1      = current
            else:
                prev2.next = current
                prev2      = current
            current = current.next
        prev2.next  = None
        prev1.next  = dummy2.next
        self.head   = dummy1.next


#  +=====================================================+
#  |                                                     |
#  |          THE TEST CODE BELOW WILL PRINT             |
#  |              OUTPUT TO "USER LOGS"                  |
#  |                                                     |
#  |  Use the output to test and troubleshoot your code  |
#  |                                                     |
#  +=====================================================+




'''
 def partition_list(self, x):
        if not self.head:
            return None
    
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head
    
        while current:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next
    
        prev1.next = None
        prev2.next = None
        prev1.next = dummy2.next
    
        self.head = dummy1.next






This function is designed to partition a linked list around 
a value x, such that all nodes with values less than x come 
before nodes with values greater than or equal to x.

Consider a sample linked list and value for partitioning:

List: 5 → 3 → 8 → 2 → 10 → 4 → 1
Partition Value (x): 4
After partitioning, the linked list should look like:

3 → 2 → 1 → 5 → 8 → 10 → 4


Method Walkthrough:

def partition_list(self, x):


Check if the list is empty:

if not self.head:
    return None
If the list is empty, there's nothing to partition, 
so we return None.



Initialize two dummy nodes and corresponding pointers:

dummy1 = Node(0)
dummy2 = Node(0)
prev1 = dummy1
prev2 = dummy2
We are going to use two separate linked lists: 
one for values less than x (handled by dummy1 and prev1) 
and another for values greater than or equal to x 
(handled by dummy2 and prev2).



Start at the head of the original list:

current = self.head
This current pointer will help us traverse the original linked list.



Traverse the list and partition the nodes:

while current:
    if current.value < x:
        prev1.next = current
        prev1 = current
    else:
        prev2.next = current
        prev2 = current
    current = current.next
We use a loop to traverse the entire linked list. 
For each node, if its value is less than x, 
we append it to the list headed by dummy1. 
If it's greater than or equal to x, we append it to the 
list headed by dummy2.



Terminate both lists:

prev1.next = None
prev2.next = None
Since we've possibly moved some nodes from the original list 
to our two new lists, we need to ensure that both new lists 
are properly terminated by setting their last node's next 
pointers to None.



Connect the two lists:

prev1.next = dummy2.next
We attach the start of the second list 
(i.e., the list of values greater than or equal to x) 
to the end of the first list.



Update the head of the linked list:

self.head = dummy1.next


We update the head of the original list to point to the head 
of our partitioned list (i.e., the first node with a value less 
than x).



Conclusion: The partition_list method efficiently partitions 
a linked list around a value x by using two temporary linked lists: 
one for nodes with values less than x and another for nodes with 
values greater than or equal to x. After partitioning, 
it connects these two lists together and updates the original 
list's head to reflect the newly partitioned list. In our example, 
the linked list gets rearranged to have all nodes less than 4 come 
before nodes with values greater than or equal to 4.





Code with inline comments:



def partition_list(self, x):
    # 1. Edge case: Check if the list is empty. If so, exit.
    if not self.head:
        return None
 
    # 2. Create two dummy nodes: 
    # dummy1 for nodes with values less than x 
    # and dummy2 for nodes with values greater or equal to x.
    dummy1 = Node(0)
    dummy2 = Node(0)
 
    # 3. Initialize two pointers (prev1 and prev2) at the dummy nodes
    # They will be used to build the two separate lists.
    prev1 = dummy1
    prev2 = dummy2
 
    # 4. Start iterating from the head of the original list.
    current = self.head
 
    # 5. Traverse the entire list.
    while current:
        # 5.1. If the current node's value is less than x:
        if current.value < x:
            # 5.1.1. Attach it to the end of the list starting at dummy1
            prev1.next = current
            # 5.1.2. Move the prev1 pointer forward.
            prev1 = current
        # 5.2. Otherwise:
        else:
            # 5.2.1. Attach it to the end of the list starting at dummy2
            prev2.next = current
            # 5.2.2. Move the prev2 pointer forward.
            prev2 = current
        
        # 5.3. Move to the next node in the original list.
        current = current.next
 
    # 6. End the two lists. 
    # Set the next pointers of prev1 and prev2 to None.
    prev1.next = None
    prev2.next = None
 
    # 7. Link the end of the first list 
    # (the one that started at dummy1) 
    # to the beginning of the second list 
    # (the one that started at dummy2).
    prev1.next = dummy2.next
 
    # 8. Update the head of the linked list to point to the beginning 
    # of the partitioned list.
    self.head = dummy1.next

'''


# Function to convert linked list to Python list
def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

# Function to test partition_list
def test_partition_list():
    test_cases_passed = 0
    
    print("-----------------------")
    
    # Test 1: Normal Case
    print("Test 1: Normal Case")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    ll.append(5)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3, 4, 5]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 2: All Equal Values
    print("Test 2: All Equal Values")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(3)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3, 3, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 3: Single Element
    print("Test 3: Single Element")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 4: Already Sorted
    print("Test 4: Already Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 5: Reverse Sorted
    print("Test 5: Reverse Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(2)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 3, 2]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 6: All Smaller Values
    print("Test 6: All Smaller Values")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(1)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 1, 1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 7: Single Element, Equal to Partition
    print("Test 7: Single Element, Equal to Partition")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Summary
    print(f"{test_cases_passed} out of 7 tests passed.")


# Run the test function
test_partition_list()
      

