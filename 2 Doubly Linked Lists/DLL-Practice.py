'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:        #OR  if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail      = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None    
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp           = self.tail
            self.tail      = self.tail.prev
            self.tail.next = None
            temp.prev      = None
            self.length   -= 1
        return temp
    



my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(8)
my_doubly_linked_list.append(9)
my_doubly_linked_list.pop()
my_doubly_linked_list.print_list()
'''
###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail      = self.tail.prev
            self.tail.next = None
            temp.prev      = None
        self.length -= 1
        return temp




my_doubly = DoublyLinkedList(1)
my_doubly.append(2)
my_doubly.pop()
my_doubly.print_list()
'''
###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail      = self.tail.prev
            self.tail.next = None
            temp.prev      = None
        self.length -= 1
        return temp
    

dll = DoublyLinkedList(0)
dll.append(1)
dll.append(2)
dll.pop()
dll.print_list()
'''
###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail      = self.tail.prev
            temp.prev      = None
            self.tail.next = None
        self.length -= 1
        return temp
    

dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.pop()
dll.print_list()

'''
###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail      = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail      = self.tail.prev
            temp.prev      = None
            self.tail.next = None
        self.length -= 1
        return temp
    
dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.pop()
dll.print_list()
'''
###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail      = self.tail.prev
            self.tail.next = None
            temp.next      = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next  = self.head
            self.head.prev = new_node
            self.head      = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head    
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head      = self.head.next
            self.head.prev = None
            temp.next      = None
        self.length -= 1
        return temp


dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.pop()
dll.prepend(0)
dll.pop_first()
dll.print_list()
'''

###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail      = self.tail.prev
            self.tail.next = None
            temp.prev      = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next  = self.head
            self.head.prev = new_node
            self.head      = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head      = self.head.next
            self.head.prev = None
            temp.next      = None
        self.length -= 1
        return temp
    

dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.pop()
dll.prepend(0)
dll.pop_first()
dll.print_list()

'''
###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail      = self.tail.prev
            self.tail.next = None
            temp.prev      = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next  = self.head
            self.head      = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head      = self.head.next
            self.head.prev = None
            temp.next      = None
        self.length -= 1
        return temp
    
dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.pop()
dll.prepend(0)
dll.pop_first()
dll.print_list()

'''
###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail      = self.tail.prev
            temp.prev      = None
            self.tail.next = None            
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next  = self.head
            self.head.prev = new_node
            self.head      = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head      = self.head.next
            self.head.prev = None
            temp.next      = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length /2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp


dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.pop()
dll.prepend(0)
dll.pop_first()
dll.print_list()
print(dll.get(1))
print(dll.get(2))

'''
###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail      = self.tail.prev
            temp.prev      = None
            self.tail.next = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next  = self.head
            self.head.prev = new_node
            self.head      = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head      = self.head.next
            temp.next      = None
            self.head.prev = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length /2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp


dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.pop()
dll.prepend(0)
dll.pop_first()
dll.print_list()
print(dll.get(1))
print(dll.get(0))

    '''

###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node  
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)  
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail      = self.tail.prev
            temp.prev      = None
            self.tail.next = None   
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next  = self.head
            self.head.prev = new_node
            self.head      = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head      = self.head.next
            temp.next      = None
            self.head.prev = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length /2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node      = Node(value)
        before        = self.get(index -1)
        after         = before.next
        new_node.prev = before  
        new_node.next = after
        before.next   = new_node
        after.prev    = new_node
        self.length  += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next      = None
        temp.prev      = None
        self.length   -= 1
        return temp


dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.pop()
dll.prepend(0)
dll.pop_first()
dll.set_value(0, 'A')
dll.insert(1, 8)
dll.remove(1)
dll.print_list()

'''

###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail           
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail      = self.tail.prev
            self.tail.next = None
            temp.prev      = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next  = self.head
            self.head.prev = new_node
            self.head      = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head      = self.head.next
            self.head.prev = None
            temp.next      = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length /2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before   = self.get(index -1)
        after    = before.next
        new_node.prev = before
        new_node.next = after
        before.next   = new_node
        after.prev    = new_node
        self.length  += 1
        return True 


    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        temp           = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next      = None
        temp.prev      = None
        self.length   -= 1
        return temp

dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(3)
dll.pop()
dll.prepend(0)
dll.pop_first()
dll.set_value(1, 8)
dll.insert(2, 9)
dll.remove(1)
dll.print_list()
# print(dll.get(1))
'''

###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            temp.prev = None
            self.tail.next = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length /2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before   = self.get(index -1)
        after    = before.next
        new_node.prev = before
        new_node.next = after
        before.next   = new_node
        after.prev    = new_node
        self.length  += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp


dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(3)
dll.pop()
dll.prepend(0)
dll.prepend(0)
dll.pop_first()
dll.set_value(1, 'X')
dll.insert(4, 'Z')
dll.remove(4)
dll.remove(1)
dll.insert(1, 1)
dll.print_list()
# print(dll.get(1))         
'''

###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length /2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(-1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node      = Node(value)
        before        = self.get(index -1)
        after         = before.next
        new_node.prev = before
        new_node.next = after
        after.prev    = new_node
        before.next   = new_node
        self.length  += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        temp           = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.prev      = None
        temp.next      = None
        self.length   -= 1
        return temp
    


dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(3)
dll.pop()
dll.prepend(0)
dll.pop_first()
dll.set_value(1, 11)
dll.insert(1, 22)
dll.remove(1)
dll.print_list()
# print(dll.get(2))
'''

###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(f'{temp.value}', end = ' ' )
            temp = temp.next
        print() # to add a new line after the above list is printed

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if self.length == 0:
            return self.prepned(value)
        if self.length == 1:
            return self.append(value)
        new_node = Node(value)
        before   = self.get(index -1)
        after    = before.next 
        before.next = new_node
        after.prev  = new_node
        new_node.next = after
        new_node.prev = before
        self.length   += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.prev = None
        temp.next = None
        self.length -= 1
        return temp



dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.pop()
dll.prepend(0)
dll.pop_first()
dll.set_value(1, 3)
dll.insert(1, 2)
dll.remove(1)
dll.print_list()
# print(dll.get(1))
'''

###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(f'{temp.value}', end = ' ')
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:           
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next  = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length /2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        after = self.get(index -1)
        before = after.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev  = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        temp   = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp



dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.pop()
dll.prepend(0)
dll.pop_first()
dll.insert(1, 9)
dll.remove(1)
dll.print_list()
# print(dll.get(1))
'''

###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(f'{temp.value}', end = ' ')
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            temp.prev = None
            self.tail.next = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length /2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(-1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index -1)
        after = before.next
        new_node.next = after
        new_node.prev = before
        after.prev = new_node
        before.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp


dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.pop()
dll.prepend(0)
dll.pop_first()
dll.set_value(0, 'P')
dll.insert(1, 'U')
dll.remove(1)
dll.print_list()
# print(dll.get(2))

'''

###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(f'{temp.value}', end = ' ')
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            temp.prev = None
            self.tail.next = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:    
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if temp.value < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index -1)
        after = before.next
        before.next = new_node
        after.prev = new_node
        new_node.prev = before
        new_node.next = after
        self.length += 1
        return True


    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.prev = None
        temp.next = None
        self.length -= 1
        return temp


dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.pop()
dll.insert(1, 3)
dll.remove(2)
dll.prepend(0)
dll.set_value(2, 2)
dll.print_list()
'''

###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(f'{temp.value}', end = ' ')
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail      = self.tail.prev
            self.tail.next = None
            temp.prev      = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next  = self.head
            self.head.prev = new_node
            self.head      = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head      = self.head.next
            temp.next      = None
            self.head.prev = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node      = Node(value)
        before        = self.get(index -1)
        after         = before.next
        before.next   = new_node
        after.prev    = new_node
        new_node.next = after
        new_node.prev = before

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp


dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.pop()
dll.prepend(0)
dll.prepend(0)
dll.pop_first()
dll.set_value(1, 'A')
dll.insert(1, 'B')
dll.remove(1)
dll.print_list()
# print(dll.get(1))
'''

###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(f'{temp.value}', end = ' ')
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next  = self.head
            self.head.prev = new_node
            self.head      = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head      = self.head.next
            self.head.prev = None
            temp.next      = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before   = self.get(index -1)
        after    = before.next

        new_node.next = after
        new_node.prev = before
        after.prev    = new_node
        before.next   = new_node  
        self.length  += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        temp = self.get(index)        
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next      = None
        temp.prev      = None
        self.length   -= 1
        return temp

    

dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.pop()
dll.prepend(0)
dll.prepend(0)
dll.pop_first()
dll.set_value(1, 'X')
dll.insert(1, 'Y')
dll.remove(3)
dll.print_list()
# print(dll.get(1))

'''
###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(f'{temp.value}', end=" ")
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail      = self.tail.prev
            self.tail.next = None
            temp.prev      = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next  = self.head
            self.head.prev = new_node
            self.head      = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head      = self.head.next
            self.head.prev = None
            temp.next      = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before   = self.get(index -1)
        after    = before.next
        new_node.next = after
        new_node.prev = before
        after.prev    = new_node
        before.next   = new_node
        self.length  += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next      = None
        temp.prev      = None
        self.length   -= 1
        return temp


dll = DoublyLinkedList(3)
dll.append(2)
dll.append(2)
dll.pop()
dll.prepend(0)
dll.prepend(0)
dll.pop_first()
dll.set_value(1, 1)
dll.insert(1, 0)
dll.remove(1)
dll.print_list()
# print(dll.get(1))

'''
###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None
    

class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(f'{temp.value}', end= " ")
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail      = self.tail.prev
            temp.prev      = None
            self.tail.next = None
        self.length   -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next  = self.head
            self.head.prev = new_node
            self.head      = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head      = self.head.next
            self.head.prev = None
            temp.next      = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before   = self.get(index -1)
        after    = before.next
        new_node.next = after
        new_node.prev = before
        after.prev    = new_node
        before.next   = new_node
        self.length  += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.next
        temp.prev.next = temp.prev
        temp.next      = None
        temp.prev      = None
        self.length   -= 1
        return temp
    


dll = DoublyLinkedList(4)
dll.append(3)
dll.append(3)
dll.pop()
dll.prepend(2)
dll.pop_first()
dll.insert(1, 0)
dll.print_list()
'''
###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None
    

class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp:
            print(f'{temp.value}', end=" ")
            temp = temp.next

    def append(self, value):
        new_value = Node(value)
        if not self.head:
            self.head = new_value
            self.tail = new_value
        else:
            self.tail.next = new_value
            new_value.prev = self.tail
            self.tail      = new_value
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.tail      = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next  = self.head
            self.head.prev = new_node
            self.head      = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head      = self.head.next
            self.head.prev = None
            temp.next      = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before   = self.get(index -1)
        after    = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev  = new_node
        
        self.length  += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        
        temp = self.get(index)
        
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp
    

dll = DoublyLinkedList(4)
dll.append(3)
dll.append(3)
dll.pop()
dll.prepend(2)
dll.pop_first()
dll.insert(1, 0)
dll.print_list()
'''
###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1
    
    def print_doubly(self):
        temp = self.head
        while temp:
            print(f'{temp.value}', end= " ")
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            temp.prev = None
            self.tail.next = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_item(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before   = self.get(index -1)
        after    = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev  = new_node
        
        self.length  += 1
        return True
    
    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        
        temp = self.get(index)
        
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp
    


dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.pop()
dll.prepend(0)
dll.pop_first()
dll.set_item(1, 'Y')
dll.insert(1, 2)
dll.remove(2)
dll.print_doubly()
# print(dll.get(1))
'''
###############################################################
###############################################################
###############################################################

class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(f'{temp.value}', end=" ")
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp

    def set_item(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before   = self.get(index - 1)
        after    = before.next

        new_node.next = before.next
        new_node.prev = before
        before.next = new_node
        after.prev  = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        temp = self.get(index)
        
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp




dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.pop()
dll.prepend(0)
dll.pop_first()
dll.set_item(1, 'Y')
dll.insert(1, 2)
dll.remove(2)
dll.print_list()
