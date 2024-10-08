"""
BST: Kth Smallest Node ( ** Interview Question)

Given a binary search tree, find the kth smallest element in the tree. For example, if the tree contains the elements [1, 2, 3, 4, 5], the 3rd smallest element would be 3.

The solution to this problem usually involves traversing the tree in-order (left, root, right) and keeping track of the number of nodes visited until you find the kth smallest element. There are two main approaches to doing this:

Iterative approach using a stack: This approach involves maintaining a stack of nodes that still need to be visited, starting with the leftmost node. At each step, you pop a node off the stack, decrement the kth smallest counter, and check whether you have found the kth smallest element. If you have not, you continue traversing the tree by moving to the right child of the current node.

Recursive approach: This approach involves recursively traversing the tree in-order and keeping track of the number of nodes visited until you find the kth smallest element. You can use a helper function that takes a node and a value of k as input, and recursively calls itself on the left and right children of the node until it finds the kth smallest element.

Both of these approaches have their own advantages and disadvantages, and the best approach to use may depend on the specific problem constraints and the interviewer's preferences.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    # WRITE KTH_SMALLEST METHOD HERE #
    #                                #
    #                                #
    #                                #
    #                                #
    ##################################
    def kth_smallest(self, k):
        values = []
        def traverse(node):
            if node is None: return
            if node.left:
                traverse(node.left)
            values.append(node.value)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        
        return values[k-1] # because we start at 1 index here



bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print(bst.kth_smallest(1))  # Expected output: 2
print(bst.kth_smallest(3))  # Expected output: 4
print(bst.kth_smallest(6))  # Expected output: 7


"""
    EXPECTED OUTPUT:
    ----------------
    2
    4
    7

 """

"""
Think about how to traverse the binary search tree in-order (left, root, right).

Use a stack to keep track of the nodes that still need to be visited, starting with the leftmost node.

Pop nodes off the stack and decrement the k counter until you find the kth smallest element.

Remember that you need to start counting from 1 for the smallest element.

Return the value of the kth smallest node when you find it, or return None if the kth smallest element does not exist (i.e., k is greater than the number of nodes in the tree).

"""

"""
    def kth_smallest(self, k):
        stack = []
        node = self.root
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.value
            
            node = node.right
            
        return None


The kth_smallest method is a method of the BinarySearchTree class that finds the kth smallest element in a binary search tree. It takes one argument, k, which is the index of the element you want to find (starting from 1 for the smallest element).

Here's how the method works:

It initializes a stack to hold nodes and sets a temporary node to the root of the tree.

It uses a while loop to traverse the tree in-order (left, root, right) and add each node to the stack.

It pops a node from the stack and decrements the k counter.

If k is equal to 0, it returns the value of the node, which is the kth smallest element.

If k is not equal to 0, it moves to the right child of the node and continues traversing the tree.

If it reaches the end of the tree without finding the kth smallest element, it returns None.

The in-order traversal guarantees that the elements will be visited in ascending order, so popping elements off the stack will give you the kth smallest element. The method uses a stack to keep track of the nodes that still need to be visited, starting with the leftmost node. When it pops a node off the stack, it decrements the k counter and checks whether it has found the kth smallest element. If it has, it returns the value of the node. If it has not, it continues traversing the tree by moving to the right child of the current node.

Overall, the kth_smallest method is an efficient way to find the kth smallest element in a binary search tree, with a time complexity of O(h + k), where h is the height of the tree.





Code with inline comments:

   

    def kth_smallest(self, k):
        # create a stack to hold nodes
        stack = []    
        # start at the root of the tree      
        temp = self.root    
        
        while stack or temp:
            # traverse to the leftmost node
            while temp: 
                # add the node to the stack                
                stack.append(temp)      
                temp = temp.left
            
            # pop the last node added to the stack
            temp = stack.pop()           
            k -= 1
            # if kth smallest element is found, return the value
            if k == 0:                  
                return temp.value
            
            # move to the right child of the node
            temp = temp.right           
            
        # if k is greater than the number of nodes in the tree, return None
        return None                      


Recursive solution:

   

    def kth_smallest(self, k):
        self.kth_smallest_count = 0
        return self.kth_smallest_helper(self.root, k)
 
    def kth_smallest_helper(self, node, k):
        if node is None:
            return None
 
        left_result = self.kth_smallest_helper(node.left, k)
        if left_result is not None:
            return left_result
 
        self.kth_smallest_count += 1
        if self.kth_smallest_count == k:
            return node.value
 
        right_result = self.kth_smallest_helper(node.right, k)
        if right_result is not None:
            return right_result
 
        return None


Here's how the recursive method works:

It initializes a counter for the number of nodes visited, starting from 0.

It calls the kth_smallest_helper function with the root node and the value of k.

The helper function first checks whether the current node is None. If it is, it returns None.

The helper function recursively calls itself on the left child of the current node and stores the result in left_result. If left_result is not None, it returns left_result.

If left_result is None, the helper function increments the kth_smallest_count counter and checks whether it has reached the value of k. If it has, it returns the value of the current node.

The helper function then recursively calls itself on the right child of the current node and stores the result in right_result. If right_result is not None, it returns right_result.

If right_result is None, the helper function returns None.

Overall, the recursive implementation of the in-order traversal is simpler and easier to understand than the iterative implementation using a stack. However, it may be less efficient for very large trees because of the function call overhead.



Recursive code with inline comments:



    def kth_smallest(self, k):
        # initialize the number of nodes visited to 0
        self.kth_smallest_count = 0
        # call the helper function with the root node and k
        return self.kth_smallest_helper(self.root, k)
 
    def kth_smallest_helper(self, node, k):
        if node is None:
            # if the current node is None, return None
            return None
 
        # recursively call the helper function on the left child of the node and store the result in left_result
        left_result = self.kth_smallest_helper(node.left, k)
        if left_result is not None:
            # if left_result is not None, return it
            return left_result
 
        # increment the number of nodes visited by 1
        self.kth_smallest_count += 1
        if self.kth_smallest_count == k:
            # if the kth smallest element is found, return the value of the current node
            return node.value
 
        # recursively call the helper function on the right child of the node and store the result in right_result
        right_result = self.kth_smallest_helper(node.right, k)
        if right_result is not None:
            # if right_result is not None, return it
            return right_result
 
        # if the kth smallest element is not found, return None
        return None
 

"""