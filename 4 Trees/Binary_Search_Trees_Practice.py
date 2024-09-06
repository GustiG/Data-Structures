'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):    # O(log N) -> divide et impera
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True     # to not run the code continuously
        temp = self.root
        while True:         # will break by the return statement
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



my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
'''

##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
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
        while True:
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

bst = BinarySearchTree()
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(0)
print(bst.root.left.value)
print(bst.root.value)
print(bst.root.right.value)
print(bst.root.right.right.value)
'''                

##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if temp.value == new_node.value:
                return False
            if new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


bst = BinarySearchTree()
bst.insert(4)
bst.insert(2)
bst.insert(3)
bst.insert(6)
bst.insert(5)
print(bst.root.value)
print(bst.root.left.value)
print(bst.root.left.right.value)
print(bst.root.right.value)
print(bst.root.right.left.value)
print(bst.contains(5))
'''

##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right
        
    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

my_tree = BinarySearchTree()
my_tree.insert(3)
my_tree.insert(2)
my_tree.insert(4)
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.contains(1))
print(my_tree.contains(2))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
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
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right

            
    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

bst = BinarySearchTree()
bst.insert(3)
bst.insert(4)
bst.insert(2)
print(bst.root.value)
print(bst.root.left.value)
print(bst.root.right.value)
print(bst.contains(1))
print(bst.contains(2))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
my_bst = BinarySearchTree()
my_bst.insert(4)
my_bst.insert(2)
my_bst.insert(3)
my_bst.insert(7)
print(my_bst.root.value)
print(my_bst.root.left.value)
print(my_bst.root.left.right.value)
print(my_bst.root.right.value)
print(my_bst.contains(9))
print(my_bst.contains(2))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
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
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


my_tree = BinarySearchTree()
my_tree.insert(3)
my_tree.insert(1)
my_tree.insert(5)
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.contains(2))
print(my_tree.contains(5))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    

my_tree = BinarySearchTree()
my_tree.insert(4)
my_tree.insert(2)
my_tree.insert(6)
my_tree.insert(0)
print(my_tree.root.left.left.value)
print(my_tree.contains(0))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    

bst = BinarySearchTree()
bst.insert(4)
bst.insert(6)
bst.insert(2)
bst.insert(1)
print(bst.root.left.left.value)
print(bst.contains(1))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        while True:
            if new_node.value == self.root.value:
                return False
            elif new_node.value < self.root.value:
                if self.root.left is None:
                    self.root.left = new_node
                    return True
                self.root = self.root.left
            else:
                if self.root.right is None:
                    self.root.right = new_node
                    return True
                self.root = self.root.right
        
    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


bst = BinarySearchTree()
bst.insert(3)
bst.insert(3)
bst.insert(2)
bst.insert(4)
print(bst.root.value)
print(bst.root.left.value)
print(bst.root.right.value)
print(bst.contains(1))
print(bst.contains(2))
'''

##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinrySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    

bst = BinrySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(5)
bst.insert(6)
print(bst.root.right.right.value)
print(bst.contains(5))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
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
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(6)
bst.insert(2)
bst.insert(7)
bst.insert(9)

print(bst.root.left.left.value)
print(bst.root.right.right.value)
print(bst.contains(2))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
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
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

bst = BinarySearchTree()
bst.insert(5)
bst.insert(6)
bst.insert(3)
bst.insert(9)

print(bst.root.right.right.value)
print(bst.contains(9))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:        
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right
            
    def contains(self, value):      #search method
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
bst = BinarySearchTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)

print(bst.root.left.left.value)
print(bst.contains(1))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
bst = BinarySearchTree()
bst.insert(3)
bst.insert(5)
bst.insert(2)
bst.insert(8)
print(bst.root.right.right.value)
print(bst.contains(8))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False            
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
bst = BinarySearchTree()
bst.insert(3)
bst.insert(2)
bst.insert(6)
print(bst.root.left.value)
print(bst.root.right.value)
print(bst.contains(2))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(6)
bst.insert(8)
print(bst.root.right.right.value)
print(bst.contains(8))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
        

bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(5)
print(bst.root.left.left.left.value)
print(bst.contains(5))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
    
    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    

bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(5)
print(bst.root.left.left.left.value)
print(bst.contains(5))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
    
    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    


bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(5)
print(bst.root.left.left.left.value)
print(bst.contains(5))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
    
    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    

bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(5)
print(bst.root.left.left.left.value)
print(bst.contains(5))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None
    

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
    
    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    

    
bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(5)
print(bst.root.left.left.left.value)
print(bst.contains(5))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    

bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(5)
print(bst.root.left.left.left.value)
print(bst.contains(5))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
        
    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    
bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(5)
print(bst.root.left.left.left.value)
print(bst.contains(5))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
    
    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    

bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(5)
print(bst.root.left.left.left.value)
print(bst.contains(5))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
    
    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    

bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(5)
print(bst.root.left.left.left.value)
print(bst.contains(5))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
    
    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(5)
print(bst.root.left.left.left.value)
print(bst.contains(5))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
    
    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    

bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(5)
print(bst.root.left.left.left.value)
print(bst.contains(5))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
    

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(5)
print(bst.root.left.left.left.value)
print(bst.contains(5))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
                    
    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False



bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(5)
print(bst.root.left.left.left.value)
print(bst.contains(5))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
    
    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    

bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(5)
print(bst.root.left.left.left.value)
print(bst.contains(5))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
    
    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    


bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(5)
print(bst.root.left.left.left.value)
print(bst.contains(5))
'''
##############################################################
##############################################################
##############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(5)
print(bst.root.left.left.left.value)
print(bst.contains(5))
'''

##############################################################
##############################################################
##############################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                else:
                    temp = temp.right
        

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False



bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(5)
print(bst.root.left.left.left.value)
print(bst.contains(5))
'''

##############################################################
##############################################################
##############################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, value):
        newNode = Node(value)
        if not self.root:
            self.root = newNode
            return True
        temp = self.root
        while True:
            if newNode.value == temp.value:
                return False
            elif newNode.value < temp.value:
                if not temp.left:
                    temp.left = newNode
                    return True
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = newNode
                    return True
                else:
                    temp = temp.right
            

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False



bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(5)
print(bst.root.left.left.left.value)
print(bst.contains(5))
'''

##############################################################
##############################################################
##############################################################

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root

        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
    

    def contains(self, value):
        temp = self.root

        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False



bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(5)
print(bst.root.left.left.left.value)
print(bst.contains(5))
'''

##############################################################
##############################################################
##############################################################

#''' STARTING THE RECURSIVE BINARY SEARCH TREE IMPLEMENTATION
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root

        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right


    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


    def __r_contains(self, current_node, value):
        if current_node == None: 
            return False
        if current_node.value == value:
            return True

        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)


    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    


    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)    # creates the new node
        
        if value < current_node.value:
            current_node.left =\
            self.__r_insert(current_node.left, value)

        if value > current_node.value:
            current_node.right =\
            self.__r_insert(current_node.right, value)
        
        return current_node # the parent node until the root


    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

        

my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(25)
my_tree.r_insert(82)

print("BST Contains 27:")
print(my_tree.r_contains(27))

print("\nBST Contains 17:")
print(my_tree.r_contains(17))

#'''
##############################################################
##############################################################
##############################################################
 