# # implement a stack using a list:
# class Stack:
#     def __init__(self):
#         self.stack_list = []

#     def push(self, value):
#         self.stack_list.append(value)

############################################################################################        
############################################################################################                    
############################################################################################        
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class Stack:
    def __init__(self, value):
        new_node    = Node(value)
        self.top    = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(f'{temp.value}')
            temp = temp.next
    
    def push(self, value):
        new_node = Node(value)
        if not self.top:            # or if height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top      = new_node
        self.height      += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        temp      = self.top
        self.top  = self.top.next
        temp.next = None
        self.height -= 1
        return temp

my_stack = Stack(4)
my_stack.push(3)
my_stack.pop()
my_stack.pop()
my_stack.print_stack()
'''

###################################################################        
###################################################################                    
###################################################################        
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class Stack:
    def __init__(self, value):
        new_node    = Node(value)
        self.top    = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    
    def pop(self):
        if self.height == 0:
            return None
        temp        = self.top
        self.top    = self.top.next
        temp.next   = None
        self.height += 1
        return temp
    

stk = Stack(4)
stk.push(3)
stk.push(2)
stk.push(2)
stk.pop()
stk.print_stack()

'''
###################################################################        
###################################################################                    
###################################################################        
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class Stack:
    def __init__(self, value):
        new_node    = Node(value)
        self.top    = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top      = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp         = self.top
        self.top     = self.top.next
        temp.next    = None
        self.height -= 1
        return temp
    
my_stack = Stack(3) 
my_stack.push(2)
my_stack.push(1)
my_stack.pop()
my_stack.print_stack()
'''
###################################################################
###################################################################
###################################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class Stack:
    def __init__(self, value):
        new_node    = Node(value)
        self.top    = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    
my_stack = Stack(3)
my_stack.push(2)
my_stack.push(1)
my_stack.pop()
my_stack.print_stack()
'''    
###################################################################
###################################################################   
###################################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class Stack:
    def __init__(self, value):
        new_node    = Node(value)
        self.top    = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
    
    def push(self, value):
        new_node = Node(value)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top      = new_node
        self.height += 1
        
    def pop(self):
        if self.height == 0:
            return None
        temp         = self.top
        self.top     = self.top.next
        temp.next    = None
        self.height -= 1

my_stack = Stack(0)
my_stack.push(1)
my_stack.push(2)
my_stack.pop()
my_stack.print_stack()
'''
###################################################################
###################################################################   
###################################################################

class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class Stack:
    def __init__(self, value):
        new_node    = Node(value)
        self.top    = new_node
        self.height = 1
    
    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node      = Node(value)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top      = new_node
        self.height  += 1

    def pop(self):
        if self.height == 0:
            return None
        temp         = self.top
        self.top     = self.top.next
        temp.next    = None
        self.height -= 1
        return temp


my_stack = Stack(1)
my_stack.push(2)
my_stack.push(3)
my_stack.pop()
my_stack.print_stack()