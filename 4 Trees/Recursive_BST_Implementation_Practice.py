'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left =\
            self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right =\
            self.__r_insert(current_node.right, value)
        return current_node


    def r_insert(self, value):
        if not self.root:
            self.root = Node(value)
        self.__r_insert(self.root, value)


    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)


    def r_contains(self, value):
        return self.__r_contains(self.root, value)



myTree = BinarySearchTree()
myTree.r_insert(2)
myTree.r_insert(1)
myTree.r_insert(3)
print(myTree.root.left.value)
print(myTree.r_contains(1))
'''

###############################################################
###############################################################
###############################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        

    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        
        if value < current_node.value:
            current_node.left =\
            self.__r_insert(current_node.left, value)

        if value > current_node.value:
            current_node.right =\
            self.__r_insert(current_node.right, value)
        return current_node    

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)


my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)
print(my_tree.root.left.value)
print(my_tree.r_contains(1))
'''

###############################################################
###############################################################
###############################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)


    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        
        if value < current_node.value:
            current_node.left =\
            self.__r_insert(current_node.left, value)
        
        if value > current_node.value:
            current_node.right =\
            self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if not self.root:
            self.root = Node(value)
        self.__r_insert(self.root, value)




my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)
print(my_tree.root.left.value)
print(my_tree.r_contains(1))

'''

###############################################################
###############################################################
###############################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        

    def r_contains(self, value):
        return self.__r_contains(self.root, value)


    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        
        if value < current_node.value:
            current_node.left =\
            self.__r_insert(current_node.left, value)
        elif value > current_node.value:
            current_node.right =\
            self.__r_insert(current_node.right, value)
        return current_node 


    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__r_insert(self.root, value)


    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        
        if value < current_node.value:
            current_node.left =\
            self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = \
            self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and\
            current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)        
                current_node.value = sub_tree_min
                current_node.right =\
                self.__delete_node(current_node.right, sub_tree_min)
        return current_node


    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)

    
    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    




my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print(my_tree.root.left.value)
my_tree.delete_node(21)
print(my_tree.root.left.value)
'''

###############################################################
###############################################################
###############################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value == current_node.value:
            return False
        
        if value < current_node.value:
            current_node.left =\
            self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right =\
            self.__r_insert(current_node.right, value)
        
        return current_node
    

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        return self.__r_insert(self.root, value)


    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        
        
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    

    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        
        if value < current_node.value:
            current_node.left =\
            self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right =\
            self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and\
              current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                replace = self.min_value(current_node.right)
                current_node.value = replace
                current_node.right =\
                self.__delete_node(current_node.right, replace)
            return current_node


    def delete_node(self, value):
        self.__delete_node(self.root, value)


    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value




my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)


print(my_tree.root.left.value)
my_tree.delete_node(21)
print(my_tree.root.left.value)
'''    

###############################################################
###############################################################
###############################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)    


    def r_contains(self, value):
        return self.__r_contains(self.root, value)


    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        
        if value < current_node.value:
            current_node.left =\
            self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right =\
            self.__r_insert(current_node.right, value)
        return current_node
    

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        return self.__r_insert(self.root, value)


    def __delete_node(self, current_node, value):
        if current_node == None:
            return None

        if value < current_node.value:
            current_node.left =\
            self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right =\
            self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and\
            current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                self.__delete_node(current_node.right, sub_tree_min)
        return current_node

    def delete_node(self, value):
        return self.__delete_node(self.root, value)


    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value
                


my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print(my_tree.root.left.value)
my_tree.delete_node(21)
print(my_tree.root.left.value)

'''

###############################################################
###############################################################
###############################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)


    def r_contains(self, value):
        return self.__r_contains(self.root, value)


    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)

        if value < current_node.value:
            current_node.left =\
            self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right =\
            self.__r_insert(current_node.right, value)
        return current_node
    

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        return self.__r_insert(self.root, value)


    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    

    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        
        if value < current_node.value:
            current_node.left =\
            self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right =\
            self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and\
            current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right =\
                self.__delete_node(current_node.right, sub_tree_min)
        return current_node
    

    def delete_node(self, value):
        return self.__delete_node(self.root, value)
        


my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print(my_tree.root.left.value)
my_tree.delete_node(21)
print(my_tree.root.left.value)
'''

###############################################################
###############################################################
###############################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True

        if value < current_node.value:
            return self.__r_contains(current_node.left, value)        
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
    

    def r_contains(self, value):
        return self.__r_contains(self.root, value)


    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        
        if value < current_node.value:
            current_node.left =\
            self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right =\
            self.__r_insert(current_node.right, value)
        return current_node
    

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        return self.__r_insert(self.root, value)


    def __delete_node(self, current_node, value):
        if current_node == None:
            return None

        if value < current_node.value:
            current_node.left =\
            self.__delete_node(current_node.left, value)    
        elif value > current_node.value:
            current_node.right =\
            self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and\
            current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right =\
                self.__delete_node(current_node.right, sub_tree_min)
        return current_node
    

    def delete_node(self, value):
        return self.__delete_node(self.root, value)


    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value



my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print(my_tree.root.left.value)
my_tree.delete_node(21)
print(my_tree.root.left.value)
'''

###############################################################
###############################################################
###############################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        

    def r_contains(self, value):
        return self.__r_contains(self.root, value)


    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        
        if value < current_node.value:
            current_node.left =\
            self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right =\
            self.__r_insert(current_node.right, value)
        return current_node
    

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        return self.__r_insert(self.root, value)


    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        
        if value < current_node.value:
            current_node.left =\
            self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right =\
            self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and\
            current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_min_tree = self.min_value(current_node.right)
                current_node.value = sub_min_tree
                current_node.right =\
                self.__delete_node(current_node.right, sub_min_tree)
        return current_node
    

    def delete_node(self, value):
        return self.__delete_node(self.root, value)


    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value



my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print(my_tree.root.left.value)
my_tree.delete_node(21)
print(my_tree.root.left.value)
'''

###############################################################
###############################################################
###############################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        

    def r_contains(self, value):
        return self.__r_contains(self.root, value)


    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        
        if value < current_node.value:
            current_node.left =\
            self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right =\
            self.__r_insert(current_node.right, value)
        return current_node
    

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        return self.__r_insert(self.root, value)


    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        
        if value < current_node.value:
            current_node.left =\
            self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right =\
            self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and\
            current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right =\
                self.__delete_node(current_node.right, sub_tree_min)
        return current_node
    

    def delete_node(self, value):
        return self.__delete_node(self.root, value)


    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value

        

my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print(my_tree.root.left.value)
my_tree.delete_node(21)
print(my_tree.root.left.value)
'''

###############################################################
###############################################################
###############################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    
class BinarySearchTree:
    def __init__(self):
        self.root = None


    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

        
    def r_contains(self, value):
        return self.__r_contains(self.root, value)


    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)

        if value < current_node.value:
            current_node.left =\
            self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right =\
            self.__r_insert(current_node.right, value)
        return current_node
    

    def r_insert(self, value):
        if not self.root:
            self.root = Node(value)
        return self.__r_insert(self.root, value)


    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        
        if value < current_node.value:
            current_node.left =\
            self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right =\
            self.__delete_node(current_node.right, value)
        else:
            if not current_node.left and not current_node.right:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right =\
                self.__delete_node(current_node.right, sub_tree_min)
        return current_node    
        

    def delete_node(self, value):
        return self.__delete_node(self.root, value)

    
    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value



my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print(my_tree.root.left.value)
my_tree.delete_node(21)
print(my_tree.root.left.value)
'''

###############################################################
###############################################################
###############################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True

        if value < current_node.value:
            return self.__r_contains(current_node.left, value)        
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        

    def r_contains(self, value):
        return self.__r_contains(self.root, value)


    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)

        if value < current_node.value:
            current_node.left =\
            self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right =\
            self.__r_insert(current_node.right, value)
        return current_node


    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)        
        return self.__r_insert(self.root, value)


    def __delete_node(self, current_node, value):
        if current_node == None:
            return None

        if value < current_node.value:
            current_node.left =\
            self.__delete_node(current_node.left, value)     
        elif value > current_node.value:
            current_node.right =\
            self.__delete_node(current_node.right, value)
        else:
            if not current_node.left and not current_node.right:
                return None
            elif not current_node.left:
                current_node = current_node.right
            elif not current_node.right:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right =\
                self.__delete_node(current_node.right, sub_tree_min)
        return current_node


    def delete_node(self, value):    
        return self.__delete_node(self.root, value)


    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value


    def BFS(self):
        current_node = self.root
        queue = []
        result = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return result



my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print(my_tree.root.left.value)
my_tree.delete_node(21)
print(my_tree.root.left.value)
print(my_tree.BFS())
'''

###############################################################
###############################################################
###############################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def __r_contains(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        

    def r_contains(self, value):
        return self.__r_contains(self.root, value)


    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)

        if value < current_node.value:
            current_node.left =\
            self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right =\
            self.__r_insert(current_node.right, value)
        return current_node
    

    def r_insert(self, value):
        if not self.root:
            self.root = Node(value)
        return self.__r_insert(self.root, value)


    def __delete_node(self, current_node, value):
        if current_node is None:
            return None
        
        if value < current_node.value:
            current_node.left =\
            self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right =\
            self.__delete_node(current_node.right, value)
        else:
            if not current_node.left and not current_node.right:
                return None
            elif not current_node.left:
                current_node = current_node.right
            elif not current_node.right:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right =\
                self.__delete_node(current_node.right, sub_tree_min)
        return current_node
    

    def delete_node(self, value):
        return self.__delete_node(self.root, value)

    
    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value
    

    def BFS(self):
        node = self.root
        queue = []
        queue.append(node)
        result = []

        while queue:
            node = queue.pop(0)
            result.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result



my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print(my_tree.r_contains(47))
print(my_tree.root.left.value)
my_tree.delete_node(21)
print(my_tree.root.left.value)
print(my_tree.BFS())
'''

###############################################################
###############################################################
###############################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def __r_contains(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
    

    def r_contains(self, value):
        return self.__r_contains(self.root, value)


    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        
        if value < current_node.value:
            current_node.left =\
            self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right =\
            self.__r_insert(current_node.right, value)
        
        return current_node
    

    def r_insert(self, value):
        if not self.root:
            self.root = Node(value)
        return self.__r_insert(self.root, value)


    def __delete_node(self, current_node, value):
        if current_node is None:
            return None
        
        if value < current_node.value:
            current_node.left =\
            self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right =\
            self.__delete_node(current_node.right, value)
        else:
            if not current_node.left and not current_node.right:
                return None
            elif not current_node.left:
                current_node = current_node.right
            elif not current_node.right:
                current_node = current_node.left
            else:
                subtree_min = self.min_value(current_node.right)
                current_node.value = subtree_min
                current_node.right =\
                self.__delete_node(current_node.right, subtree_min)
        return current_node
    

    def delete_node(self, value):
        return self.__delete_node(self.root, value)


    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value
    

    def BFS(self):
        node = self.root
        queue = []
        queue.append(node)
        result = []

        while queue:
            node = queue.pop(0)
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result


my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print(my_tree.r_contains(47))
print(my_tree.root.left.value)
my_tree.delete_node(21)
print(my_tree.root.left.value)
print(my_tree.BFS())
'''

###############################################################
###############################################################
###############################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.left, value)


    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    
    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)

        if value < current_node.value:
            current_node.left =\
            self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right =\
            self.__r_insert(current_node.right, value)

        return current_node
    

    def r_insert(self, value):
        if not self.root:
            self.root = Node(value)
        return self.__r_insert(self.root, value)


    def __delete_node(self, current_node, value):
        if current_node == None:
            return None

        if value < current_node.value:
            current_node.left =\
            self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right =\
            self.__delete_node(current_node.right, value)
        else:
            if not current_node.left and not current_node.right:
                return None
            elif not current_node.left:
                current_node = current_node.right
            elif not current_node.right:
                current_node = current_node.left
            else:
                subtree_min = self.min_value(current_node.right)
                current_node.value = subtree_min
                current_node.right =\
                self.__delete_node(current_node.right, subtree_min)
    
        return current_node
    
        
    def delete_node(self, value):
        return self.__delete_node(self.root, value)


    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value


    def BFS(self):
        node = self.root
        queue = []
        queue.append(node)
        result = []

        while len(queue) > 0:
            node = queue.pop(0)
            result.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
        return result


    def dfs_pre_order(self):
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
        traverse(self.root)
        return results


    def dfs_post_order(self):
        results = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results
    

    def dfs_in_order(self):
        results = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)
        traverse(self.root)
        return results
    


my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print(my_tree.r_contains(47))
print(my_tree.root.left.value)
print(my_tree.BFS())
print(my_tree.dfs_pre_order())
print(my_tree.dfs_post_order())
print(my_tree.dfs_in_order())
my_tree.delete_node(21)
print(my_tree.root.left.value)
'''

###############################################################
###############################################################
###############################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    
    def __r_contains(self, current_node, value):
        if not current_node: 
            return False
        if value == current_node.value: 
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
    

    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    

    def __r_insert(self, current_node, value):
        if not current_node:
            return Node(value)
        
        if value < current_node.value:
            current_node.left =\
            self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right =\
            self.__r_insert(current_node.right, value)    
        return current_node
    

    def r_insert(self, value):
        if not self.root:
            self.root = Node(value)
        return self.__r_insert(self.root, value)
    

    def __delete_node(self, current_node, value):
        if not current_node:
            return None
        
        if value < current_node.value:
            current_node.left =\
            self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right =\
            self.__delete_node(current_node.right, value)
        else:
            if not current_node.left and not current_node.right:
                return None
            elif not current_node.left:
                current_node = current_node.right
            elif not current_node.right:
                current_node = current_node.left
            else:
                subtree_min = self.min_value(current_node.right)
                current_node.value = subtree_min
                current_node.right =\
                self.__delete_node(current_node.right, subtree_min)
    
        return current_node
    

    def delete_node(self, value):
        return self.__delete_node(self.root, value)


    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value
    

    def BFS(self):
        node = self.root
        queue = []
        queue.append(node)
        results = []

        while len(queue) > 0:
            node = queue.pop(0)
            results.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return results
    

    def dfs_pre_order(self):
        results = []
        def traverse(node):
            results.append(node.value)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(self.root)    
        return results
    

    def dfs_post_order(self):
        results = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            results.append(node.value)
        traverse(self.root)
        return results
    

    def dfs_in_order(self):
        results = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            results.append(node.value)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return results
    


my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print(my_tree.r_contains(47))
print(my_tree.root.left.value)
print(my_tree.BFS())
print(my_tree.dfs_pre_order())
print(my_tree.dfs_post_order())
print(my_tree.dfs_in_order())
my_tree.delete_node(21)
print(my_tree.root.left.value)
'''

###############################################################
###############################################################
###############################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    
    def __r_contains(self, current_node, value):
        if not current_node:
            return False
        if value == current_node.value:
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    
    def r_contains(self, value):
        return self.__r_contains(self.root, value)


    def __r_insert(self, node, value):
        if not node:
            return Node(value)
        
        if value < node.value:
            node.left = self.__r_insert(node.left, value)
        if value > node.value:
            node.right = self.__r_insert(node.right, value)
        
        return node
    

    def r_insert(self, value):
        if not self.root:
            self.root = Node(value)
        return self.__r_insert(self.root, value)


    def __delete_node(self, node, value):
        if not node:
            return None
        
        if value < node.value:
            node.left = self.__delete_node(node.left, value)
        elif value > node.value:
            node.right = self.__delete_node(node.right, value)
        else:
            if not node.left and not node.right:
                return None
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                subtree_min = self.min_value(node.right)
                node.value = subtree_min
                node.right = self.__delete_node(node.right, subtree_min)
        return node
    

    def delete_node(self, value):
        return self.__delete_node(self.root, value)

    
    def min_value(self, node):
        while node.left:
            node = node.left
        return node.value
    

    def BFS(self):
        node = self.root
        queue = []
        queue.append(node)
        results = []
        while len(queue) > 0:
            node = queue.pop(0)
            results.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return results
    

    def dfs_pre_order(self):
        results = []
        def traverse(node):
            results.append(node.value)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return results


    def dfs_post_order(self):
        results = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            results.append(node.value)
        traverse(self.root)
        return results
    

    def dfs_in_order(self):
        results = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            results.append(node.value)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return results
    


my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print(my_tree.r_contains(47))
print(my_tree.root.left.value)
print(my_tree.BFS())    # prints in the order the values were added
print(my_tree.dfs_pre_order()) # prints by dfs rules order -- 
# starts with one branch, gets both leaves and moves to the next
print(my_tree.dfs_post_order()) # prints from the leaves to the root
print(my_tree.dfs_in_order()) # prints in ascending order
my_tree.delete_node(21)
print(my_tree.root.left.value)
'''

###############################################################
###############################################################
###############################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        
    
    def r_contains(self, value):
        return self.__r_contains(self.root, value)


    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)

        if value < current_node.value:
            current_node.left =\
            self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right =\
            self.__r_insert(current_node.right, value)
        
        return current_node
    

    def r_insert(self, value):
        if not self.root:
            self.root = Node(value)
        return self.__r_insert(self.root, value)


    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        
        if value < current_node.value:
            current_node.left =\
            self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right =\
            self.__delete_node(current_node.right, value)
        else:
            if not current_node.left and not current_node.right:
                return None
            elif not current_node.left:
                current_node = current_node.right
            elif current_node.right:
                current_node = current_node.left
            else:
                subtree_min = self.min_value(current_node.right)
                current_node.value = subtree_min
                current_node.right =\
                self.__delete_node(current_node.right, subtree_min)
        return current_node
    

    def delete_node(self, value):
        return self.__delete_node(self.root, value)

    
    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value
    

    def BFS(self):
        node = self.root
        queue = []
        queue.append(node)
        results = []

        while len(queue) > 0:
            node = queue.pop(0)
            results.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return results
    

    def dfs_pre_order(self):
        results = []
        def traverse(node):
            results.append(node.value)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return results
    

    def dfs_post_order(self):
        results = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            results.append(node.value)
        traverse(self.root)
        return results


    def dfs_in_order(self):
        results = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            results.append(node.value)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return results
    


my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print(my_tree.r_contains(47))
print(my_tree.root.left.value)
print(my_tree.BFS())    # prints by row starting at the root
print(my_tree.dfs_pre_order()) # prints by dfs rules order -- 
# starts from the root, gets down to the leaves
print(my_tree.dfs_post_order()) # prints from the leaves to the root
print(my_tree.dfs_in_order()) # prints in ascending order
my_tree.delete_node(21)
print(my_tree.root.left.value)
'''

###############################################################
###############################################################
###############################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    
    def __r_contains(self, node, value):
        if not node: 
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self.__r_contains(node.left, value)
        if value > node.value:
            return self.__r_contains(node.right, value)
        

    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    

    def __r_insert(self, node, value):
        if not node:
            return Node(value)
        if value < node.value:
            node.left = self.__r_insert(node.left, value)
        if value > node.value:
            node.right = self.__r_insert(node.right, value)
        return node
    

    def r_insert(self, value):
        if not self.root:
            self.root = Node(value)
        return self.__r_insert(self.root, value)
    

    def __delete_node(self, node, value):
        if not node:
            return None
        if value < node.value:
            node.left = self.__delete_node(node.left, value)
        elif value > node.value:
            node.right = self.__delete_node(node.right, value)
        else:
            if not node.left and not node.right:
                return None
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                subtree_min = self.min_val(node.right)
                node.value = subtree_min
                node.right =\
                      self.__delete_node(node.right, subtree_min)
        return node
    

    def delete_node(self, value):
        return self.__delete_node(self.root, value)
    

    def min_val(self, node):
        while node.left:
            node = node.left
        return node.value


    def BST(self):
        node = self.root
        queue = []
        queue.append(node)
        results = []
        while len(queue) > 0:
            node = queue.pop(0)
            results.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return results
    

    def dfs_pre_order(self):
        results = []
        def traverse(node):
            results.append(node.value)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return results
    
     
    def dfs_post_order(self):
        results = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            results.append(node.value)
        traverse(self.root)
        return results


    def dfs_in_order(self):
        results = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            results.append(node.value)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return results



my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print(my_tree.r_contains(47))
print(my_tree.root.left.value)
print(my_tree.BFS(), "-> Breadth First Search")
print(my_tree.dfs_pre_order(), "-> Depth F. S. Pre Order")
print(my_tree.dfs_post_order(), "-> Depth F. S. Post Order")
print(my_tree.dfs_in_order(), "-> DFS in order (ascending)")
my_tree.delete_node(21)
print(my_tree.root.left.value)

'''

###############################################################
###############################################################
###############################################################

#'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    
    def __r_contains(self, node, value):
        if not node:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self.__r_contains(node.left)
        if value > node.value:
            return self.__r_contains(node.right)
    

    def r_contains(self, value):
        return self.__r_contains(self.root, value)
        

    def __r_insert(self, node, value):
        if not node:
            return Node(value)
        if value < node.value:
            node.left = self.__r_insert(node.left, value)
        if value > node.value:
            node.right = self.__r_insert(node.right, value)
        return node
    

    def r_insert(self, value):
        if not self.root:
            self.root = Node(value)
        return self.__r_insert(self.root, value)
    

    def __delete_node(self, node, value):
        if not node:
            return None
        if value < node.value:
            node.left = self.__delete_node(node.left, value)
        elif value > node.value:
            node.right = self.__delete_node(node.right, value)
        else:
            if not node.left and not node.right:
                return None
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                subtree_min = self.min_val(node.right)
                node.value = subtree_min
                node.right =\
                     self.__delete_node(node.right, subtree_min)
        return node
    

    def delete_node(self, value):
        return self.__delete_node(self.root, value)


    def min_val(self, node):
        while node.left:
            node = node.left
        return node.value
    

    def BFS(self):
        node = self.root
        queue = []
        queue.append(node)
        results = []
        while len(queue) > 0:
            node = queue.pop(0)
            results.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return results
    

    def dfs_pre_order(self):
        results = []
        def traverse(node):
            results.append(node.value)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return results


    def dfs_post_order(self):
        results = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            results.append(node.value)
        traverse(self.root)
        return results


    def dfs_in_order(self):
        results = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            results.append(node.value)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return results


    def dfs_desc(self):
        results = []
        def traverse(node):
            if node.right:
                traverse(node.right)
            results.append(node.value)
            if node.left:
                traverse(node.left)
        traverse(self.root)
        return results
    

my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print(my_tree.r_contains(47))
print(my_tree.root.left.value)
print(my_tree.BFS(), "-> Breadth First Search")
print(my_tree.dfs_pre_order(), "-> Depth F. S. Pre Order")
print(my_tree.dfs_post_order(), "-> Depth F. S. Post Order")
print(my_tree.dfs_in_order(), "-> DFS in order (ascending)")
print(my_tree.dfs_desc(), "-> DFS from max value to min")
my_tree.delete_node(21)
print(my_tree.root.left.value)
#'''

###############################################################
###############################################################
###############################################################