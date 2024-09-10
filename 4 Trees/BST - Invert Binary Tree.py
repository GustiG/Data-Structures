"""
BST: Invert Binary Tree ( ** Interview Question)
Objective: Write a method to invert (or mirror) a binary tree. This means that for every node in the binary tree, you will swap its left and right children.

Method Signature:

def __invert_tree(self, node):



Input:

node: A Node object representing the root of a binary tree. The Node class has attributes value, left, and right, where value is the value stored in the node, and left and right are pointers to the node's left and right children, respectively.



Output:

The root node of the inverted binary tree.



Requirements:

The method must be recursive. It should work by traversing the tree and swapping the left and right children of every node encountered.

If the input tree is empty (i.e., node is None), the method should return None.

The inversion should happen in-place, meaning you should not create a new tree but instead modify the existing tree structure.

The method should handle binary trees of any size and structure, ensuring that every node's left and right children are swapped.

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
                  
    def __r_insert(self, current_node, value):
        if current_node == None: 
            return Node(value)   
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:  # Changed to elif to avoid comparing twice if equal
            current_node.right = self.__r_insert(current_node.right, value) 
        return current_node    

    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        else:
            self.__r_insert(self.root, value)  

    def invert(self):
        self.root = self.__invert_tree(self.root)

    #   +===================================================+
    #   |              WRITE YOUR CODE HERE                 |
    #   | Description:                                      |
    #   | - Private method to invert a binary tree.         |
    #   | - It swaps every left child with its right child  |
    #   |   recursively.                                    |
    #   |                                                   |
    #   | Parameters:                                       |
    #   | - node: The current node being visited.           |
    #   |                                                   |
    #   | Return:                                           |
    #   | - The node after its subtree has been inverted.   |
    #   |                                                   |
    #   | Tips:                                             |
    #   | - The function works recursively, swapping left   |
    #   |   and right children of all nodes in the tree.    |
    #   | - A temporary variable is used to facilitate the  |
    #   |   swap of the children.                           |
    #   +===================================================+
    def __invert_tree(self, node):
        if not node: 
            return None
        temp = node.left 
        node.left = self.__invert_tree(node.right)
        node.right = self.__invert_tree(temp)
        return node


#  +====================================================+  
#  |  Test code below will print output to "User logs"  |
#  +====================================================+ 

def tree_to_list(node):
    """Helper function to convert tree to list level-wise for easy comparison"""
    if not node:
        return []
    queue = [node]
    result = []
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.value)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
    while result and result[-1] is None:  # Clean up trailing None values
        result.pop()
    return result

def test_invert_binary_search_tree():
    print("\n--- Testing Inversion of Binary Search Tree ---")
    # Define test scenarios
    scenarios = [
        ("Empty Tree", [], []),
        ("Single Node", [1], [1]),
        ("Tree with Left Child", [2, 1], [2, None, 1]),
        ("Tree with Right Child", [1, 2], [1, 2]),
        ("Multi-Level Tree", [3, 1, 5, 2], [3, 5, 1, None, None, 2]),
        ("Invert Twice", [4, 2, 6, 1, 3, 5, 7], [4, 2, 6, 1, 3, 5, 7]),
    ]

    for description, setup, expected in scenarios:
        bst = BinarySearchTree()
        for num in setup:
            bst.r_insert(num)
        if description == "Invert Twice":
            bst.invert()  # First inversion
        bst.invert()  # Perform inversion (or second inversion for the specific case)
        result = tree_to_list(bst.root)
        print(f"\n{description}: {'Pass' if result == expected else 'Fail'}")
        print(f"Expected: {expected}")
        print(f"Actual:   {result}")

test_invert_binary_search_tree()

"""
Pseudo Code:



Define __invert_tree Method

Input: node (a node in the binary tree)

Output: The root node of the inverted binary tree

Check for Base Case

If node is None (indicating an empty tree or the end of a branch),

Return None

Swap Left and Right Children

Save the current node's left child in a temporary variable (temp)

Assign the result of recursively inverting the right child to the current node's left child

Assign the result of recursively inverting the saved left child (now in temp) to the current node's right child

Return the Current Node

After the left and right children have been swapped, return the current node to ensure the inverted structure is maintained up the tree





METHOD __invert_tree(node)
    IF node IS None
        RETURN None
    ENDIF
    
    SET temp TO node.left
    SET node.left TO __invert_tree(node.right)
    SET node.right TO __invert_tree(temp)
    
    RETURN node

"""

"""
SOLUTION:

def __invert_tree(self, node):
        if node is None:
            return None
    
        temp = node.left
        node.left = self.__invert_tree(node.right)
        node.right = self.__invert_tree(temp)
        
        return node




The method __invert_tree takes a single argument, node, which represents a node in a binary tree.

The goal of the method is to swap the left and right children of every node in the tree, effectively mirroring the tree's structure.

Here's a step-by-step explanation of how it works:



Base Case Check: The method starts by checking if the node is None. This check serves as the base case for the recursion, ensuring that the method stops recursing when it reaches the end of a branch (i.e., a leaf node's children, which are None). If the node is None, the method returns None, indicating that there's nothing to invert at this level of recursion.

Swapping Children: Before swapping the children of the current node, the method saves the current node's left child in a temporary variable temp. This step is crucial because the inversion process involves overwriting the node's left child, and we need to preserve the original left child for later use.

Recursive Inversion: The method then recursively calls itself to invert the right child of the current node, assigning the result to the node's left child. This effectively starts the inversion process, where the right subtree of the current node becomes its left subtree after inversion.

Completing the Swap: Using the original left child saved in temp, the method makes another recursive call to invert this subtree. The result of this inversion is assigned to the node's right child, completing the swap. Now, the original left subtree of the current node becomes its right subtree after inversion.

Returning the Node: Finally, the method returns the current node. At this point, the node's left and right children have been swapped (inverted), and the method continues to propagate up the recursion stack, inverting the rest of the tree. By returning the node, the method ensures that the structure of the inverted tree is maintained, allowing the inverted children to be correctly reattached to their parent nodes.



The overall effect of this method is to create a mirror image of the original binary tree by swapping the left and right subtrees at every node. This inversion is applied recursively to all nodes in the tree, starting from the root node passed into the method.





Code with inline comments:



def __invert_tree(self, node):
    # Check if the current node is None. This happens when the tree is empty
    # or we've reached a leaf node's child. It's the base case for our recursion.
    if node is None:
        return None
    
    # Before swapping, save the original left child of the node in a temporary
    # variable. This is crucial because we're about to overwrite node.left with
    # the inverted right subtree, and we need to preserve the original left subtree
    # for inverting it next.
    temp = node.left
 
    # Recursively invert the right subtree of the current node and assign it
    # to the left child of the current node. This begins the process of swapping
    # the left and right children of the node.
    node.left = self.__invert_tree(node.right)
 
    # Now, invert the original left subtree (which we've saved in temp) and assign
    # it to the right child of the current node. This completes the swapping process.
    # Note that we use the preserved original left subtree for this, ensuring that
    # each child is correctly inverted and placed.
    node.right = self.__invert_tree(temp)
    
    # Return the current node. Now that its children have been swapped (inverted),
    # it's part of the newly inverted tree structure. This return statement allows
    # the recursion to work its way up, inverting each node's children from the bottom
    # of the tree to the top.
    return node

"""