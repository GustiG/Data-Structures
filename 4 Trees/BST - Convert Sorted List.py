"""
BST: Convert Sorted List to Balanced BST ( ** Interview Question)
Objective:

The task is to develop a method that takes a sorted list of integers as input and constructs a height-balanced BST.

This involves creating a BST where the depth of the two subtrees of any node does not differ by more than one.

Achieving a height-balanced tree is crucial for optimizing the efficiency of tree operations, ensuring that the BST remains efficient for search, insertion, and deletion across all levels of the tree.



Method Overview: __sorted_list_to_bst

Input: A sorted list of integers nums, provided in ascending order. The input list represents a sequential collection of elements to be transformed into a BST. The method also receives two additional parameters, left and right, which denotes the current segment of the list being processed.

Process: The method __sorted_list_to_bst employs a divide-and-conquer strategy to construct the BST. It identifies the middle element of the current list segment to serve as the subtree's root, ensuring that the resulting BST is height-balanced. The method recursively applies this logic to the left and right halves of the list, building up the BST from the bottom up.

Output: The root node of a height-balanced BST constructed from the sorted list. This node links to all other nodes in the BST, effectively representing the entire tree structure.



Requirements:

The BST must maintain the binary search tree property: for any given node, all values in the left subtree must be less than the node's value, and all values in the right subtree must be greater.

The resulting BST should be height-balanced to optimize the efficiency of subsequent operations performed on the tree.



Implementation Details:

The class BinarySearchTree encapsulates the functionality needed to construct and manage a BST, including the method sorted_list_to_bst which serves as the public interface for converting a sorted list into a BST.

The method __sorted_list_to_bst is a recursive helper function designed for internal use within the class. It directly supports the construction process by dividing the list and building the tree to ensure it is height-balanced.



If you are having difficulty understanding the process of repeatedly breaking the list in half recursively, it might be helpful to you to watch the Merge Sort section and then come back to this exercise.

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # The 'is_balanced' and 'inorder_traversal' methods will 
    # be used to test your code
    def is_balanced(self, node=None):
        def check_balance(node):
            if node is None:
                return True, -1
            left_balanced, left_height = check_balance(node.left)
            if not left_balanced:
                return False, 0
            right_balanced, right_height = check_balance(node.right)
            if not right_balanced:
                return False, 0
            balanced = abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)
            return balanced, height

        balanced, _ = check_balance(self.root if node is None else node)
        return balanced
        
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        result = []
        self._inorder_helper(node, result)
        return result
    
    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)
                
                
    def sorted_list_to_bst(self, nums):
        self.root = self.__sorted_list_to_bst(nums, 0, len(nums) - 1)

        #   +====================================================+
        #   |               WRITE YOUR CODE HERE                 |
        #   | Description:                                       |
        #   | - Private method to convert a sorted list to a     |
        #   |   binary search tree (BST).                        |
        #   | - The method uses the middle element of the list   |
        #   |   as the root to ensure balanced height.           |
        #   |                                                    |
        #   | Parameters:                                        |
        #   | - nums: Sorted list of integers.                   |
        #   | - left: Starting index of the list segment.        |
        #   | - right: Ending index of the list segment.         |
        #   |                                                    |
        #   | Return:                                            |
        #   | - The root node of the BST created from the        |
        #   |   specified list segment.                          |
        #   |                                                    |
        #   | Tips:                                              |
        #   | - The function is recursively called to construct  |
        #   |   the left and right subtrees.                     |
        #   | - A new Node is created at each recursive call     |
        #   |   with the mid element of the current list segment |
        #   |   as its value, ensuring the BST property is       |
        #   |   maintained.                                      |
        #   +====================================================+
    def __sorted_list_to_bst(self, nums, left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        current = Node(nums[mid])

        current.left =\
        self.__sorted_list_to_bst(nums, left, mid - 1)
        current.right =\
        self.__sorted_list_to_bst(nums, mid + 1, right)

        return current



#  +====================================================+  
#  |  Test code below will print output to "User logs"  |
#  +====================================================+ 

def check_balanced_and_correct_traversal(bst, expected_traversal):
    is_balanced = bst.is_balanced()
    inorder = bst.inorder_traversal()
    print("Is balanced:", is_balanced)
    print("Inorder traversal:", inorder)
    print("Expected traversal:", expected_traversal)
    if is_balanced and inorder == expected_traversal:
        print("PASS: Tree is balanced and inorder traversal is correct.\n")
    else:
        print("FAIL: Tree is either not balanced or inorder traversal is incorrect.\n")

# Test: Convert an empty list
print("\n----- Test: Convert Empty List -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([])
check_balanced_and_correct_traversal(bst, [])

# Test: Convert a list with one element
print("\n----- Test: Convert Single Element List -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([10])
check_balanced_and_correct_traversal(bst, [10])

# Test: Convert a sorted list with odd number of elements
print("\n----- Test: Convert Sorted List with Odd Number of Elements -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([1, 2, 3, 4, 5])
check_balanced_and_correct_traversal(bst, [1, 2, 3, 4, 5])

# Test: Convert a sorted list with even number of elements
print("\n----- Test: Convert Sorted List with Even Number of Elements -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([1, 2, 3, 4, 5, 6])
check_balanced_and_correct_traversal(bst, [1, 2, 3, 4, 5, 6])

# Test: Convert a large sorted list
print("\n----- Test: Convert Large Sorted List -----\n")
bst = BinarySearchTree()
large_sorted_list = list(range(1, 16))  # A list from 1 to 15
bst.sorted_list_to_bst(large_sorted_list)
check_balanced_and_correct_traversal(bst, large_sorted_list)


"""
Pseudo Code:



Define the __sorted_list_to_bst method

Input: sorted list nums, left boundary left, right boundary right.

Check if sub-list is empty

If left > right, return None.

Find middle element

Calculate middle index mid as (left + right) // 2.

Create node with middle element

Create a new node current with value nums[mid].

Construct left subtree

Recursively call __sorted_list_to_bst for left part of list (left, mid - 1) and assign to current.left.

Construct right subtree

Recursively call __sorted_list_to_bst for right part of list (mid + 1, right) and assign to current.right.

Return current node

The current node becomes root of BST subtree for given sub-list.


"""

"""
SOLUTION:

def __sorted_list_to_bst(self, nums, left, right):
        if left > right:
            return None
            
        mid = (left + right) // 2
        current = Node(nums[mid])
        
        current.left = self.__sorted_list_to_bst(nums, left, mid - 1)
        current.right = self.__sorted_list_to_bst(nums, mid + 1, right)
        
        return current




The method converts a sorted list nums into a balanced binary search tree and returns the root node of this tree.

Let's break down the method step by step:



Input Parameters:

nums: A sorted list of elements from which the BST is to be created.

left and right: The indices in nums that define the current segment being considered. Initially, left is 0, and right is the length of the list minus one.

Base Case Check:

if left > right:: This checks if the current segment is valid. If left is greater than right, it means the segment is empty (this can happen in recursive calls when the segment has been fully processed), and there's no node to create for this segment. Hence, it returns None.

Finding the Middle Element:

mid = (left + right) // 2: This calculates the middle index of the current segment. Since the list is sorted, choosing the middle element to be the root of the BST or subtree helps ensure the resulting tree is balanced. A balanced tree maintains an approximately equal number of nodes on both sides of any given node, which optimizes search times.

Creating the Node:

current = Node(nums[mid]): A new node is created with the value from the middle of the segment. This node will either be the root of the BST (in the first call) or the root of a subtree in subsequent recursive calls.

Building the Left Subtree:

current.left = self.__sorted_list_to_bst(nums, left, mid - 1): This recursively calls the same method to process the left half of the current segment (all elements before the middle element). The return value, which is the root of the left subtree, is assigned to the left attribute of the current node. This ensures all elements in the left subtree are less than the root.

Building the Right Subtree:

current.right = self.__sorted_list_to_bst(nums, mid + 1, right): Similarly, this line recursively processes the right half of the segment (all elements after the middle element). The root of the right subtree is assigned to the right attribute of the current node, ensuring all elements in the right subtree are greater than the root.

Returning the Node:

The method concludes by returning current, which is now the root node of a balanced BST (or subtree) constructed from the current segment of the list.



In essence, this method uses a divide-and-conquer approach, recursively splitting the sorted list into halves, and using the middle element of each segment to construct a node in the BST. This ensures the resulting BST is balanced, with each node's left and right children correctly representing elements less than and greater than the node's value, respectively.



Code with inline comments:



def __sorted_list_to_bst(self, nums, left, right):
    # Base condition: if left index is greater than right index,
    # it means we have considered all elements in this segment.
    # So, return None because there's no more node to create.
    if left > right:
        return None
        
    # Find the middle index of the current segment of the list.
    # This step is crucial for creating a balanced BST because
    # choosing the middle element as the root node ensures that
    # the number of nodes in the left and right subtrees are
    # as equal as possible.
    mid = (left + right) // 2
    
    # Create a new Node instance using the value at the middle index.
    # This node becomes the root of the BST (or subtree in recursive calls)
    # for the current segment of the list. The choice of the middle element
    # as the node's value is what allows the BST to be balanced.
    current = Node(nums[mid])
    
    # Recursively build the left subtree. To do this, the function calls
    # itself with the current segment adjusted to the left half, excluding
    # the middle element. This constructs the left part of the tree, ensuring
    # that elements lesser than the root are placed in the left subtree.
    current.left = self.__sorted_list_to_bst(nums, left, mid - 1)
    
    # Similarly, recursively build the right subtree by adjusting the
    # segment to the right half of the current list, beyond the middle
    # element. This ensures that elements greater than the root are
    # correctly placed in the right subtree.
    current.right = self.__sorted_list_to_bst(nums, mid + 1, right)
    
    # After constructing both left and right subtrees, return the
    # current node. This node is now the root of a balanced subtree
    # with its left and right children properly assigned.
    # In the context of recursive calls, this step effectively
    # builds up the tree from bottom to top, ensuring that each
    # recursive call returns a subtree that is correctly linked
    # to its parent node as either a left or right child.
    return current

"""