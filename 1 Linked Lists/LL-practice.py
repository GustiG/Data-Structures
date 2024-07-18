# create a simple linked list class made up of
# Node class and LinkedList class
# Node will contain the node constructor (value + pointer to None)
# LinkedList will contain the newly created node, 
# a head, tail and a length of 1

# class Node:
#     def __init__ (self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__ (self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

# my_linked_list = LinkedList(4)

# print("The value  = ", my_linked_list.tail.value)   # workaround 
# print("The tail   = ", my_linked_list.tail.value)
# print("The length = ", my_linked_list.length)


##################################################################
##################################################################
##################################################################

# class Node:
#     def __init__ (self, value):
#         self.value = value
#         self.next = None
    
# class LinkedList:
#     def __init__ (self, value):
#         node_variable = Node(value)
#         self.head = node_variable
#         self.tail = node_variable
#         self.length = 1

# my_linked_list = LinkedList(3)

# print("Head   : ", my_linked_list.head.value)
# print("Tail   : ", my_linked_list.tail.value)
# print("Length : ", my_linked_list.length)



#################################################################
#################################################################
#################################################################

# class Node:
#     def __init__ (self, value):
#         self.value = value
#         self.next = None


# class LinkedList:
#     def __init__ (self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1


# my_linked_list = LinkedList(2)

# print("Head   = ", my_linked_list.head.value,
#       "\nTail   = ", my_linked_list.tail.value, 
#       "\nLength = ", my_linked_list.length)


#################################################################
#################################################################
#################################################################

# class Node:
#     def __init__ (self, value):
#         self.value = value                # create the new node
#         self.next = None                  


# class LinkedList:
#     def __init__ (self, value):
#         new_node = Node(value)              # creates a new node (pointer + value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
#     def append(self, value):                
#         new_node = Node(value)
#         if self.head is None:               # if the list is empty
#             self.head = new_node            # have tail and head point at the same node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node       # this one just points to the next new node
#             self.tail = new_node            # this one moves the tail to point at the last node
#         self.length += 1
#         return True                         # not needed as a standalone method
# my_linked_list = LinkedList(4)

# print("Head   = ", my_linked_list.head.value,
#       "\nTail   = ", my_linked_list.tail.value,
#       "\nLength = ", my_linked_list.length)

# my_linked_list.append(5)
# my_linked_list.print_list() 


#################################################################
#################################################################
#################################################################


# class Node():
#     def __init__ (self, value):
#         self.value = value
#         self.next = None

# class LinkedList():
#     def __init__ (self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

# my_linked_list = LinkedList(4)

# print("Head   = ", my_linked_list.head.value,
#       "\nTail   = ", my_linked_list.tail.value,
#       "\nLength = ", my_linked_list.length)

# my_linked_list.print_list()


#################################################################
#################################################################
#################################################################

# class Node:
#     def __init__ (self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__ (self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#         return True

# my_linked_list = LinkedList(4)

# my_linked_list.append(2)

# my_linked_list.print_list()

# print("Head   = ", my_linked_list.head.value,
#       "\nTail   = ", my_linked_list.tail.value,
#       "\nLength = ", my_linked_list.length)


#################################################################
#################################################################
#################################################################

# class Node:
#     def __init__ (self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__ (self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

#     def print_list (self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1

# my_linked_list = LinkedList(3)
# my_linked_list.append(6)

# my_linked_list.print_list()

# print("Head   = ", my_linked_list.head.value,
#       "\nTail   = ", my_linked_list.tail.value,
#       "\nLength = ", my_linked_list.length)


#################################################################
#################################################################
#################################################################


# class Node:
#     def __init__ (self, value):
#         self.value = value
#         self.next = None

# class LinkedList():
#     def __init__ (self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

#     def print_list (self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append (self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1

#     def pop (self):
#         if self.length == 0:
#             return None 
#         temp = self.head
#         pre  = self.head 
#         while (temp.next):  #  if temp.next is not None: -- if we're not at the end of the list
#             pre  = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp

# my_linked_list = LinkedList(3)
# my_linked_list.append(6)
# my_linked_list.print_list()
# my_linked_list.pop()
# my_linked_list.print_list()

#################################################################
#################################################################
#################################################################

# class Node:
#     def __init__ (self, value):
#         self.value = value
#         self.next  = None

# class LinkedList:
#     def __init__ (self, value):
#         new_node    = Node(value)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list (self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append (self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1

#     def pop (self):
#         if self.length == 0:
#             return None
#         pre  = self.head
#         temp = self.head
#         while (temp.next):
#             pre  = temp
#             temp = temp.next
#         self.tail      = pre
#         self.tail.next = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp

# my_linked_list = LinkedList(3)
# my_linked_list.append(6)
# my_linked_list.pop()

# my_linked_list.print_list()


#################################################################
#################################################################
#################################################################


# class Node:
#     def __init__ (self, value):
#         self.value = value
#         self.next  = None

# class LinkedList:
#     def __init__ (self, value):
#         new_node    = Node(value)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list (self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append (self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1

#     def pop (self):
#         if self.length == 0:
#             return None
#         pre  = self.head
#         temp = self.head
#         while (temp.next):
#             pre  = temp
#             temp = temp.next
#         self.tail      = pre
#         self.tail.next = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp

# my_linked_list = LinkedList(3)
# my_linked_list.append(6)
# my_linked_list.pop()
# my_linked_list.pop()

# my_linked_list.print_list()
# print(my_linked_list.length)


#################################################################
#################################################################
#################################################################

# class Node:
#     def __init__ (self, value):
#         self.value = value
#         self.next  = None

# class LinkedList:
#     def __init__ (self, value):
#         new_node     = Node(value)
#         self.head    = new_node
#         self.tail    = new_node
#         self.length  = 1

#     def print_list (self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append (self, value):
#         new_node = Node(value)
#         if self.head is None:   # is self.length == 0
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1

#     def pop (self):
#         if self.length == 0:
#             return None            
#         temp = self.head
#         pre  = self.head
#         while (temp.next):
#             pre  = temp
#             temp = temp.next
#         self.tail      = pre
#         self.tail.next = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp


# my_linked_list = LinkedList(3)
# my_linked_list.append(6)
# print ("Head : ", my_linked_list.head.value,
#        "\nTail : ", my_linked_list.tail.value)
# my_linked_list.pop()
# my_linked_list.pop()

# print(my_linked_list.print_list())   # None


#################################################################
#################################################################
#################################################################

# class Node:
#     def __init__ (self, value):
#         self.value = value
#         self.next  = None

# class LinkedList:
#     def __init__ (self, value):
#         new_node    = Node(value)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list (self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append (self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1

#     def pop (self):
#         if self.length == 0:
#             return None
#         pre  = self.head
#         temp = self.head
#         while (temp.next):
#             pre  = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length  -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp
    
# my_linked_list = LinkedList(3)
# my_linked_list.append(6)
# my_linked_list.pop()
# my_linked_list.print_list()


#################################################################
#################################################################
#################################################################

# class Node:
#     def __init__ (self, value):
#         self.value = value
#         self.next  = None

# class LinkedList:
#     def __init__ (self, value):
#         new_node    = Node(value) 
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list (self):
#         temp = self.head
#         while (temp is not None):
#             print(temp.value)
#             temp = temp.next

#     def append (self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1

#     def pop (self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pre  = self.head
#         while (temp.next):
#             pre  = temp
#             temp = temp.next
#         self.tail      = pre
#         self.tail.next = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp
    
# my_linked_list = LinkedList(3)
# my_linked_list.append(6)
# my_linked_list.pop()
# my_linked_list.pop()

# print(my_linked_list.print_list())

#################################################################
#################################################################
#################################################################

# class Node:
#     def __init__ (self, value):
#         self.value = value
#         self.next  = None

# class LinkedList:
#     def __init__ (self, value):
#         new_node    = Node(value) 
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list (self):
#         temp = self.head
#         while (temp is not None):
#             print(temp.value)
#             temp = temp.next

#     def append (self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1

#     def pop (self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pre  = self.head
#         while (temp.next):
#             pre  = temp
#             temp = temp.next
#         self.tail      = pre
#         self.tail.next = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp

#     def prepend (self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head     = new_node
#         self.length += 1
#         return True         # optional


# my_linked_list = LinkedList(3)
# my_linked_list.append(6)
# my_linked_list.prepend(1)
# my_linked_list.pop()
# my_linked_list.print_list()


#################################################################
#################################################################
#################################################################

# class Node:
#     def __init__ (self, value):
#         self.value = value
#         self.next  = None

# class LinkedList:
#     def __init__ (self,value):
#         new_node    = Node(value)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list (self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def prepend (self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head     = new_node
#         self.length += 1

#     def append (self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1
#         return True

#     def pop (self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pre  = self.head
#         while (temp.next):
#             pre  = temp
#             temp = temp.next
#         self.tail      = pre
#         self.tail.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp

# my_linked_list = LinkedList(3)
# my_linked_list.prepend(2)
# my_linked_list.prepend(1)
# my_linked_list.append(4)
# my_linked_list.pop()
# my_linked_list.print_list()

#################################################################
#################################################################
#################################################################

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next  = None
    
# class LinkedList:
#     def __init__(self, value):
#         new_node    = Node(value)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1 
    
#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1

#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pre  = self.head
#         while(temp.next):
#             pre  = temp
#             temp = temp.next 
#         self.tail      = pre
#         self.tail.next = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp
    
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head     = new_node
#         self.length += 1

# my_linked_list = LinkedList(3)
# my_linked_list.prepend(2)
# my_linked_list.append(4)
# my_linked_list.pop()
# my_linked_list.prepend(1)
# my_linked_list.print_list()


#################################################################
#################################################################
#################################################################

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next  = None

# class LinkedList:
#     def __init__(self, value):
#         new_node    = Node(value)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1
#         return True

#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pre  = self.head
#         while (temp.next):
#             pre  = temp
#             temp = temp.next
#         self.tail      = pre
#         self.tail.next = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp

#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head     = new_node
#         self.length += 1
#         return True

# my_linked_list = LinkedList(3)
# my_linked_list.append(4)
# my_linked_list.pop()
# my_linked_list.prepend(2)
# my_linked_list.prepend(1)
# my_linked_list.print_list()


#################################################################
#################################################################
#################################################################

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next  = None

# class LinkedList:
#     def __init__(self, value):
#         new_node    = Node(value)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1
#         return True

#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pre  = self.head
#         while(temp.next):
#             pre  = temp
#             temp = temp.next
#         self.tail      = pre
#         self.tail.next = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp

#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head     = new_node
#         self.length += 1
#         return True

# my_linked_list = LinkedList(3)
# my_linked_list.append(4)
# my_linked_list.prepend(2)
# my_linked_list.pop()
# my_linked_list.prepend(1)
# my_linked_list.print_list()


#################################################################
#################################################################
#################################################################

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next  = None

# class LinkedList:
#     def __init__(self, value):
#         new_node    = Node(value) 
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while(temp is not None):
#             print(temp.value)
#             temp = temp.next

#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1
#         return True

#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pred = self.head
#         while(temp.next):
#             pred = temp
#             temp = temp.next
#         self.tail      = pred
#         self.tail.next = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp
    
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head     = new_node
#         self.length += 1
#         return True
    
# my_linked_list = LinkedList(6)
# my_linked_list.append(4)
# my_linked_list.pop()
# my_linked_list.prepend(3)
# my_linked_list.print_list()


#################################################################
#################################################################
#################################################################

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next  = None

# class LinkedList:
#     def __init__(self, value):
#         new_node    = Node(value)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1
#         return True    

#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pred = self.head
#         while(temp.next):
#             pred = temp
#             temp = temp.next
#         self.tail      = pred
#         self.tail.next = None
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         self.length -= 1
#         return temp
    
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head     = new_node
#         self.length += 1
#         return True


# my_linked_list = LinkedList(6)
# print("Initial list:")
# my_linked_list.print_list()

# print("\nAppending 4:")
# my_linked_list.append(4)
# my_linked_list.print_list()

# print("\nPopping last element:")
# popped_node = my_linked_list.pop()
# print("Popped node value:", popped_node.value)
# my_linked_list.print_list()

# print("\nPrepending 3:")
# my_linked_list.prepend(3)
# my_linked_list.print_list()

# print("\nAppending 5:")
# my_linked_list.append(5)
# my_linked_list.print_list()

# print("\nPopping last element:")
# popped_node = my_linked_list.pop()
# print("Popped node value:", popped_node.value)
# my_linked_list.print_list()


#################################################################
#################################################################
#################################################################

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next  = None

# class LinkedList:
#     def __init__(self, value):
#         new_node    = Node(value)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while(temp is not None):
#             print(temp.value)
#             temp = temp.next
    
#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1
#         return True
    
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pred = self.head
#         while(temp.next):
#             pred = temp
#             temp = temp.next
#         self.tail      = pred
#         self.tail.next = None
#         self.length += 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp

#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head     = new_node
#         self.length += 1
#         return True
    
#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp         = self.head
#         self.head    = self.head.next
#         temp.next    = None
#         self.length -= 1
#         if self.length == 0:    #case for when the list starts at 1
#             self.tail = None    # and ends at 0
#         return temp             

# my_linked_list = LinkedList(6)
# my_linked_list.append(1)
# my_linked_list.prepend(3)
# my_linked_list.pop()
# my_linked_list.pop_first()
# my_linked_list.print_list()


#################################################################
#################################################################
#################################################################
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next  = None

# class LinkedList:
#     def __init__(self, value):
#         new_node    = Node(value)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1
#         return True
    
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pred = self.head
#         while(temp.next):
#             pred = temp
#             temp = temp.next
#         self.tail      = pred
#         self.tail.next = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp
    
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head     = new_node
#         self.length += 1
#         return True

#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp      = self.head
#         self.head = self.head.next
#         temp.next = None
#         if self.length == 0:
#             self.tail = None
#         return temp
    

# my_linked_list = LinkedList(6)
# my_linked_list.prepend(3)
# my_linked_list.pop_first()
# my_linked_list.print_list()

#################################################################
#################################################################
#################################################################


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next  = None

# class LinkedList:
#     def __init__(self, value):
#         new_node     = Node(value)
#         self.head    = new_node
#         self.tail    = new_node
#         self.length  = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1
#         return True

#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pred = self.head
#         while(temp.next):
#             pred = temp
#             temp = temp.next
#         self.tail      = pred
#         self.tail.next = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp
    
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head     = new_node
#         self.length += 1
#         return True

#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp         = self.head
#         self.head    = self.head.next
#         temp.next    = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp
    

# my_linked_list = LinkedList(6)
# my_linked_list.prepend(3)
# my_linked_list.pop_first()
# my_linked_list.prepend(3)
# my_linked_list.print_list()


#################################################################
#################################################################
#################################################################

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next  = None

# class LinkedList:
#     def __init__(self, value):
#         new_node    = Node(value)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append(self, value):
#         new_node = Node(value)
#         if self.head == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1
#         return True
    
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pred = self.head
#         while(temp.next):
#             pred = temp
#             temp = temp.next
#             self.head = pred
#         if self.length == 0:
#             self.head = 0
#             self.tail = 0
#         self.length -= 1
#         return temp
    
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         new_node.next = self.head
#         self.head     = new_node
#         self.length  += 1
#         return True
    
#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp      = self.head
#         self.head = self.head.next
#         temp.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp
    
    
# my_linked_list = LinkedList(3)
# my_linked_list.append(6)
# my_linked_list.prepend(1)
# my_linked_list.pop_first()
# my_linked_list.print_list()


#################################################################
#################################################################
#################################################################


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next  = None


# class LinkedList:
#     def __init__(self, value):
#         new_node    = Node(value)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         self.tail.next = new_node
#         self.tail      = new_node
#         self.length   += 1
#         return True
    
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pred = self.head
#         while(temp.next):
#             pred = temp
#             temp = temp.next
#         self.tail      = pred
#         self.tail.next = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp

#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         new_node.next = self.head
#         self.head      = new_node
#         self.length   += 1
#         return True

#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         self.head = self.head.next
#         temp.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp


# my_linked_list = LinkedList(6)
# my_linked_list.append(4)
# my_linked_list.pop()
# my_linked_list.prepend(3)
# my_linked_list.prepend(1)
# my_linked_list.pop_first()
# my_linked_list.print_list()

#################################################################
#################################################################
#################################################################


# class Node:
#     def __init__(self, value):
#         self.value   = value
#         self.pointer = None

# class LinkedList:
#     def __init__(self, value):
#         new_node    = Node(value)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.pointer

#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         self.tail.pointer = new_node
#         self.tail         = new_node
#         self.length      += 1
#         return True
    
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pred = self.head
#         while temp.pointer:
#             pred = temp
#             temp = temp.pointer
#         self.tail = pred
#         self.tail.pointer = None
#         self.length -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp
    
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         new_node.pointer = self.head
#         self.head        = new_node
#         self.length     += 1
#         return True
    
#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         self.head    = self.head.pointer
#         temp.pointer = None
#         self.length -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp
    

# my_linked_list = LinkedList(6)
# my_linked_list.append(9)
# my_linked_list.pop()
# my_linked_list.prepend(3)
# my_linked_list.prepend("www")
# my_linked_list.pop_first()
# my_linked_list.print_list()


#################################################################
#################################################################
#################################################################


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next  = None

# class LinkedList:
#     def __init__(self, value):
#         new_node    = Node(value)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         self.tail.next = new_node
#         self.tail      = new_node
#         self.length   += 1
#         return True
    
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pred = self.head
#         while temp.next:
#             pred = temp
#             temp = temp.next
#         self.tail = pred
#         self.tail.next = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp
    
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         new_node.next = self.head
#         self.head     = new_node
#         self.length  += 1
#         return True

#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp         = self.head
#         self.head    = self.head.next
#         temp.next    = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp 
    
# my_linked_list = LinkedList(6)
# my_linked_list.append(1)
# my_linked_list.pop()
# my_linked_list.prepend(3)
# my_linked_list.prepend("L")
# my_linked_list.pop_first()
# my_linked_list.print_list()

#################################################################
#################################################################
#################################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None

class LinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        self.tail      = new_node
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pred = self.head
        while temp.next:
            pred = temp
            temp = temp.next
        self.tail      = pred
        self.tail.next = None
        self.length   += 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            return None
        new_node.next = self.head
        self.head     = new_node
        self.length  += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp         = self.head
        self.head    = self.head.next
        temp.next    = None 
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    

my_linked_list = LinkedList(6)
my_linked_list.append(2)
my_linked_list.pop()
my_linked_list.prepend(3)
my_linked_list.prepend(1)
my_linked_list.pop_first()
my_linked_list.print_list()
'''

#################################################################
#################################################################
#################################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pred = self.head
        while temp.next:
            pred = temp
            temp = temp.next
        self.tail      = pred
        self.tail.next = None
        self.length   -= 1
        if self.length == 0:    # when we pop the last element
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next  = self.head
            self.head      = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp      = self.head
        self.head = self.head.next
        temp.next = None
        self.length   -= 1
        if self.length == 0:    # if you are poping the last element
            self.head = None
            self.tail = None
        return temp
    

my_linked_list = LinkedList(6)
my_linked_list.append("J")
my_linked_list.pop()
my_linked_list.pop()
my_linked_list.append(3)
my_linked_list.prepend(3)
my_linked_list.pop_first()
my_linked_list.append(6)
my_linked_list.print_list()

'''

#################################################################
#################################################################
#################################################################

'''class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pred = self.head
        while (temp.next):
            pred = temp
            temp = temp.next
        self.tail      = pred
        self.tail.next = None
        self.length   -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp         = self.head
        self.head    = self.head.next
        temp.next    = None
        self.length -= 1
        if self.length == 0:    # after removing the last value
            self.tail = None
        return temp
    
my_linked_list = LinkedList(6)
my_linked_list.append(4)
my_linked_list.pop()
my_linked_list.prepend(3)
my_linked_list.pop_first()
my_linked_list.print_list()
'''

#################################################################
#################################################################
#################################################################


'''class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pred = self.head
        while (temp.next):
            pred = temp
            temp = temp.next
        self.tail      = pred
        self.tail.next = None
        self.length   -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next      = None
        self.length   -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
my_linked_list = LinkedList(6)
my_linked_list.append("KK")
my_linked_list.pop()
my_linked_list.pop()
my_linked_list.prepend(6)
my_linked_list.prepend(1)
my_linked_list.pop_first()
my_linked_list.print_list()
'''

#################################################################
#################################################################
#################################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None

    
class LinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pred = self.head
        while (temp.next):
            pred = temp
            temp = temp.next
        self.tail      = pred
        self.tail.next = None
        self.length   -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp        = self.head
        self.head   = self.head.next
        temp.next   = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return True
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):  # only put a variable (i) if it's used inside the for loop
            temp = temp.next
        return temp             # temp.value to get the actual value with print

    
my_linked_list = LinkedList(6)
my_linked_list.append(4)
my_linked_list.pop()
my_linked_list.prepend(3)
my_linked_list.prepend("g")
my_linked_list.pop_first()
my_linked_list.print_list()
print(my_linked_list.get(1))

'''

#################################################################
#################################################################
#################################################################


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next  = None


# class LinkedList:
#     def __init__(self, value):
#         new_node    = Node(value)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1

#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pred = self.head
#         while(temp.next):
#             pred = temp
#             temp = temp.next
#         self.tail      = pred
#         self.tail.next = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp
    
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head     = new_node
#         self.length += 1

#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp         = self.head
#         self.head    = self.head.next
#         temp         = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp

#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp.value

# my_linked_list = LinkedList(3)
# my_linked_list.append(6)
# my_linked_list.pop()
# my_linked_list.prepend(2)
# my_linked_list.pop_first()
# my_linked_list.append(6)
# my_linked_list.print_list()
# print(my_linked_list.get(1))

#################################################################
#################################################################
#################################################################


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next  = None


# class LinkedList:
#     def __init__(self, value):
#         new_node    = Node(value)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1
#         return True
    
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pred = self.head
#         while(temp.next):
#             pred = temp
#             temp = temp.next
#         self.tail      = pred
#         self.tail.next = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp

#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head     = new_node
#         self.length += 1
#         return True

#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp         = self.head
#         self.head    = self.head.next
#         temp.next    = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp

#     def get(self, index):
#         if index < 0 or index >= self.length:   # = because the index starts at 0
#             return None
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp.value


# my_linked_list = LinkedList("A")
# my_linked_list.append("B")
# my_linked_list.pop_first()
# my_linked_list.pop_first()
# print(my_linked_list.get(0))
#LinkedList(3).print_list()



#################################################################
#################################################################
#################################################################

'''
class Node:
    def __init__ (self, value):
        self.value = value
        self.next  = None


class LinkedList:
    def __init__ (self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pred = self.head
        while temp.next:
            pred = temp
            temp = temp.next
        self.tail      = pred
        self.tail.next = None
        self.length   -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp         = self.head
        self.head    = self.head.next
        temp         = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)  # temp points to the node or None
        if temp:                # if temp is not None
            temp.value = value
            return True
        return False            # if .get returns None         


my_linked_list = LinkedList(3)
my_linked_list.append("A")
my_linked_list.set_value(1, 6)
my_linked_list.print_list()

'''

#################################################################
#################################################################
#################################################################


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next  = None


# class LinkedList:
#     def __init__(self, value):
#         new_node    = Node(value)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp:
#             print(temp.value)
#             temp = temp.next

#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1
#         return True

#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pred = self.head
#         while temp.next:
#             pred = temp
#             temp = temp.next
#         self.tail      = pred
#         self.tail.next = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp

#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head     = new_node
#         self.length += 1
#         return True


#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp         = self.head
#         self.head    = self.head.next
#         temp         = None 
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp


#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp

#     def set_value(self, index, value):
#         temp = self.get(index)
#         if temp:
#             temp.value = value
#             return True
#         return False


# my_linked_list = LinkedList(4)
# my_linked_list.append(1)
# my_linked_list.pop()
# my_linked_list.prepend(3)
# my_linked_list.pop_first()
# print(my_linked_list.get(1))
# my_linked_list.set_value(0, "A")
# my_linked_list.print_list()


#################################################################
#################################################################
#################################################################


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next  = None


# class LinkedList:
#     def __init__(self, data):
#         new_node    = Node(data)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1


#     def print_list(self):
#         temp = self.head
#         while temp:
#             print(temp.data)
#             temp = temp.next

#     def append(self, data):
#         new_node = Node(data)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1
#         return True
    
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pred = self.head
#         while temp.next:
#             pred = temp
#             temp = temp.next
#         self.tail      = pred
#         self.tail.next = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return True

#     def prepend(self, data):
#         new_node = Node(data)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head     = new_node
#         self.length += 1
#         return True

#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp         = self.head
#         self.head    = self.head.next
#         temp         = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp

#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp

#     def set_value(self, index, data):
#         temp = self.get(index)
#         if temp:
#             temp.data = data
#             return True
#         return False


# my_linked_list = LinkedList(3)
# my_linked_list.append(6)
# my_linked_list.pop()
# my_linked_list.prepend(2)
# my_linked_list.pop_first()
# my_linked_list.append(0)
# my_linked_list.set_value(1, 6)
# my_linked_list.print_list()


#################################################################
#################################################################
#################################################################

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next  = None


# class LinkedList:
#     def __init__(self, value):
#         new_node    = Node(value)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp:
#             print(temp.value)
#             temp = temp.next

#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1
#         return True
    
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pred = self.head
#         while temp.next:
#             pred = temp
#             temp = temp.next
#         self.tail      = pred
#         self.tail.next = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None

#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head, self. tail = new_node
#         new_node.next = self.head
#         self.head     = new_node
#         self.length  += 1
#         return True
        
#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp           = self.head
#         self.head      = self.head.next
#         temp           = None
#         self.length   -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp
            
#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return "Index out of range"
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp
    
#     def set_value(self, index, value):
#         temp = self.get(index)
#         if temp:
#             temp.value = value
#             return True
#         return False
    
# my_linked_list = LinkedList(3)
# my_linked_list.append(6)
# my_linked_list.pop()
# my_linked_list.prepend(1)
# my_linked_list.pop_first()
# print(my_linked_list.get(1))
# my_linked_list.set_value(0, 2)
# my_linked_list.print_list()


#################################################################
#################################################################
#################################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
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
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node       # last item points to the new node
            self.tail      = new_node       # last item becomes the new node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pred = self.head
        while temp.next:
            pred = temp
            temp = temp.next
        self.tail      = pred
        self.tail.next = None
        self.length   -= 1
        if self.length == 0:
            self.head = self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp         = self.head
        self.head    = self.head.next
        temp         = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
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
        temp          = self.get(index -1)
        new_node.next = temp.next
        temp.next     = new_node
        self.length  += 1
        return True


my_linked_list = LinkedList("A")
my_linked_list.append('B')
my_linked_list.append('c')
my_linked_list.pop()
my_linked_list.prepend(1)
my_linked_list.pop_first()
print(my_linked_list.get(2))
my_linked_list.set_value(1, 'P')
my_linked_list.insert(1, 'B')
my_linked_list.print_list()
'''
#################################################################
#################################################################
#################################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
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
            self.tail      = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pred = self.head
        while temp.next:
            pred = temp
            temp = temp.next
        self.tail      = pred
        self.tail.next = None
        temp           = temp.next
        self.length   += 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp         = self.head
        self.head    = self.head.next
        temp.next    = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
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
        temp          = self.get(index -1) 
        new_node.next = temp.next
        temp.next     = new_node
        self.length  += 1
        return True
    
my_linked_list = LinkedList('A')
my_linked_list.append('B')
my_linked_list.append('c')
my_linked_list.pop()
my_linked_list.prepend('Z')
my_linked_list.set_value(0, 'A')
my_linked_list.set_value(1, 'B')
my_linked_list.pop()
my_linked_list.append('D')
my_linked_list.insert(2, 'C')
my_linked_list.print_list()
'''

#################################################################
#################################################################
#################################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pred = self.head
        while(temp.next):
            pred = temp
            temp = temp.next
        self.tail      = pred
        self.tail.next = None
        self.length   -= 1
        if self.length == 0:
            self.head = self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp           = self.head
        self.head.next = temp
        temp.next      = None
        self.length   -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp     = self.get(index)
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
        temp          = self.get(index -1)
        new_node.next = temp.next
        temp.next     = new_node
        self.length  += 1
        return True
    
    
my_linked_list = LinkedList('A')
my_linked_list.append('B')
my_linked_list.append('c')
my_linked_list.pop()
my_linked_list.prepend('Z')
my_linked_list.set_value(0, 'A')
my_linked_list.set_value(1, 'B')
my_linked_list.pop()
my_linked_list.append('D')
my_linked_list.insert(2, 'C')
my_linked_list.print_list()
'''

#################################################################
#################################################################
#################################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
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
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pred = self.head
        while temp.next:
            pred = temp
            temp = temp.next
        self.tail      = pred
        self.tail.next = None
        self.length   += 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp         = self.head
        self.head    = self.head.next
        temp.next    = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
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
        temp          = self.get (index - 1)
        new_node.next = temp.next
        temp.next     = new_node
        self.length  += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev         = self.get(index -1)
        temp         = prev.next
        prev.next    = temp.next
        temp.next    = None
        self.length -= 1
        return temp
    

my_linked_list = LinkedList('B')
my_linked_list.append('C')
my_linked_list.prepend('A')
my_linked_list.pop()
my_linked_list.pop_first()
my_linked_list.insert(0, 'A')
my_linked_list.insert(2, 'C')
my_linked_list.remove(1)
my_linked_list.print_list()
'''
#################################################################
#################################################################
#################################################################

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next  = None


# class LinkedList:
#     def __init__(self, value):
#         new_node    = Node(value)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp:
#             print(temp.value)
#             temp = temp.next
            
#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1
#         return True
    
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         prev = self.head
#         while temp.next:
#             prev = temp
#             temp = temp.next
#         self.tail      = prev
#         self.tail.next = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp
    
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head     = new_node
#         self.length += 1
#         return True
    
#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp           = self.head
#         self.head.next = temp.next
#         temp           = None
#         self.length   -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp
    
#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp
    
#     def set_value(self, index, value):
#         temp = self.get(index)
#         if temp:
#             temp.value = value
#             return True
#         return False
    
#     def insert(self, index, value):
#         if index < 0 or index > self.length:
#             return False
#         if index == 0:
#             return self.prepend(value)
#         if index == self.length:
#             return self.append(value)
#         new_node      = Node(value)
#         temp          = self.get(index -1)
#         new_node.next = temp.next
#         temp.next     = new_node
#         self.length  += 1
#         return True
    
#     def remove(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         if self.length == 0:
#             return self.pop_first()
#         if self.length == self.length -1:
#             return self.pop()
#         prev         = self.get(index -1)
#         temp         = prev.next
#         prev.next    = temp.next
#         temp.next    = None
#         self.length -= 1
#         return temp
    

# my_linked_list = LinkedList('A')
# my_linked_list.append('B')
# my_linked_list.append('c')
# my_linked_list.pop()
# my_linked_list.insert(2, 'C')
# my_linked_list.print_list()


#################################################################
#################################################################
#################################################################


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next  = None

# class LinkedList:
#     def __init__(self, value):
#         new_node    = Node(value) 
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp:
#             print(temp.value)
#             temp = temp.next

#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1
#         return True
    
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         prev = self.head
#         while temp.next:
#             prev = temp
#             temp = temp.next
#         self.tail      = prev
#         self.tail.next = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp
    
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head     = new_node
#         self.length += 1
#         return True
    
#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp         = self.head
#         self.head    = self.head.next
#         temp.next    = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp
    
#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp
    
#     def set_value(self, index, value):
#         temp = self.get(index)
#         if temp:
#             temp.value = value
#             return True
#         return False
    
#     def insert(self, index, value):
#         if index < 0 or index > self.length:
#             return False
#         if index == 0:
#             return self.prepend(value)
#         if index == self.length:
#             return self.append(value)
#         new_node      = Node(value)
#         temp          = self.get(index -1)
#         new_node.next = temp.next
#         temp.next     = new_node
#         self.length  += 1
#         return True
    
#     def remove(self, index):
#         if index < 0 or index > self.length:
#             return None
#         if index == 0:
#             return self.pop_first()
#         if index == self.length -1:
#             return self.pop()
#         prev         = self.get(index -1)
#         temp         = prev.next
#         prev.next    = temp.next
#         temp.next    = None
#         self.length -= 1
#         return temp


# my_linked_list = LinkedList("A")
# my_linked_list.append("B")
# my_linked_list.append("C")
# my_linked_list.prepend(1)
# my_linked_list.pop_first()
# my_linked_list.remove(1)
# my_linked_list.print_list()
# my_linked_list.insert(1, "B")



#################################################################
#################################################################
#################################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None

class LinkedList:
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
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail      = prev
        self.tail.next = None
        self.length   -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp         = self.head
        self.head    = self.head.next
        temp.next    = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
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
        temp          = self.get(index -1)
        new_node.next = temp.next
        temp.next     = new_node
        self.length  += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev         = self.get(index -1)
        temp         = prev.next
        prev.next    = temp.next
        temp.next    = None
        self.length -= 1
        return temp
        
my_linkedList = LinkedList(1)
my_linkedList.append("D")
my_linkedList.pop()
my_linkedList.pop_first()
my_linkedList.prepend(3)
my_linkedList.set_value(0, 'A')
my_linkedList.insert(1, "B")
my_linkedList.remove(0)
my_linkedList.print_list()
'''

#################################################################
#################################################################
#################################################################

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next  = None


# class LinkedList:
#     def __init__(self, value):
#         new_node    = Node(value)
#         self.head   = new_node
#         self.tail   = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp:
#             print(temp.value)
#             temp = temp.next

#     def append(self, value):
#         new_node = Node(value)
#         if self.head == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail      = new_node
#         self.length += 1
#         return True
    
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         prev = None  # Initialize prev to None
#         while temp.next:
#             prev = temp
#             temp = temp.next
#         if prev:
#             prev.next = None  # Set the next of the previous node to None
#             self.tail = prev  # Update the tail to the previous node
#         else:
#             self.head = None  # If the list has only one node, set both head and tail to None
#             self.tail = None
#         self.length -= 1  # Decrement the length
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp

    
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head     = new_node
#         self.length += 1
#         return True
    
#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp           = self.head
#         self.head      = self.head.next   
#         temp.next      = None
#         self.length   -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return True
    
#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp
    
#     def set_value(self, index, value):
#         temp = self.get(index)
#         if temp:
#             temp.value = value
#             return True
#         return False
    
#     def insert(self, index, value):
#         if index < 0 or index > self.length:
#             return False
#         if index == 0:
#             return self.prepend(value)
#         if index == self.length:
#             return self.append(value)
#         new_node      = Node(value)
#         temp          = self.get(index -1)
#         new_node.next = temp.next
#         temp.next     = new_node
#         self.length  += 1
#         return True
    
#     def remove(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         if index == 0:
#             return self.pop_first()
#         if index == self.length - 1:
#             return self.pop()
#         prev = self.get(index - 1)
#         temp = prev.next
#         prev.next = temp.next  # Update the prev.next pointer to skip the node being removed
#         temp.next = None
#         self.length -= 1
#         return temp

    

# my_linked_list = LinkedList(3)
# my_linked_list.append(1)
# my_linked_list.pop()
# my_linked_list.prepend(6)
# my_linked_list.append(6)
# my_linked_list.pop()
# my_linked_list.prepend(0)
# my_linked_list.set_value(0, "A")
# my_linked_list.set_value(1, "A")
# my_linked_list.set_value(2, "A")
# my_linked_list.insert(0, 1)
# my_linked_list.insert(1, 2)
# my_linked_list.insert(2, 3)
# my_linked_list.remove(3)
# my_linked_list.remove(4)
# my_linked_list.remove(5)
# my_linked_list.remove(3)
# my_linked_list.print_list()

#################################################################
#################################################################
#################################################################
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next
        self.tail      = prev
        self.tail.next = None
        self.length   -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)    
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp         = self.head
        self.head    = self.head.next
        temp.next    = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp     = self.get(index)
        if temp is not None:
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
        temp          = self.get(index -1)
        new_node.next = temp.next
        temp.next     = new_node
        self.length  += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev         = self.get(index -1)
        temp         = prev.next
        prev.next    = temp.next
        temp.next    = None
        self.length -= 1
        return temp


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.pop()
my_linked_list.prepend(0)
my_linked_list.set_value(0,3)
my_linked_list.insert(1,6)
my_linked_list.remove(2)
my_linked_list.print_list()

'''


#################################################################
#################################################################
#################################################################

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
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
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail      = prev
        self.tail.next = None
        self.length   -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp         = self.head
        self.head    = self.head.next
        temp.next    = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
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
        temp          = self.get(index -1)
        new_node.next = temp.next
        temp.next     = new_node
        self.length  += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev         = self.get(index -1)
        temp         = prev.next
        prev.next    = temp.next
        temp.next    = None
        self.length -= 1
        return temp

    def reverse(self):
        temp      = self.head
        self.head = self.tail
        self.tail = temp
        after     = temp.next
        before    = None        
        for _ in range(self.length): # while temp is not None:
            after     = temp.next
            temp.next = before
            before    = temp
            temp      = after



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.prepend(0)
my_linked_list.reverse()
my_linked_list.print_list()
#print(my_linked_list.get(0))
'''

#################################################################
#################################################################
#################################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next
        self.tail      = prev
        self.tail.next = None
        self.length   -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp         = self.head
        self.head    = self.head.next
        temp.next    = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
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
        temp = self.get(index -1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev = self.get(index -1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp      = self.head
        self.head = self.tail
        self.tail = temp
        after     = temp.next
        before    = None
        while temp is not None: # or for _ in range(self.length)
            after     = temp.next
            temp.next = before
            before    = temp
            temp      = after


my_linked_list = LinkedList(3)
my_linked_list.append(6)
my_linked_list.pop()
my_linked_list.prepend(1)
my_linked_list.pop_first()
print(my_linked_list.get(1))
my_linked_list.set_value(0,1)
my_linked_list.insert(1,2)
my_linked_list.insert(1,"x")
my_linked_list.remove(1)
my_linked_list.reverse()
my_linked_list.print_list()
'''

#################################################################
#################################################################
#################################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
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
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail      = prev
        self.tail.next = None
        self.length   -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        temp         = self.head
        self.head    = self.head.next
        temp.next    = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range (index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        while temp:
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
        temp          = self.get(index -1)
        new_node.next = temp.next
        temp.next     = new_node
        self.length  += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == index -1:
            return self.pop()
        prev = self.get(index -1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp      = self.head
        self.head = self.tail
        self.tail = temp
        before    = None
        after     = temp.next
        while temp:             # for _ in range(self.length)
            after     = temp.next
            temp.next = before
            before    = temp
            temp      = after

    

my_linked_list = LinkedList('A')
my_linked_list.prepend(9)
my_linked_list.pop_first()
my_linked_list.append('B')
my_linked_list.set_value(1, 'C')
my_linked_list.insert(1, 'B')
my_linked_list.remove(1)
my_linked_list.insert(1, 'B')
my_linked_list.reverse()
my_linked_list.print_list()
#print(my_linked_list.get(0))

'''
#################################################################
#################################################################
#################################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
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
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length   -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp      = self.head
        self.head = self.head.next
        temp.next = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(self.length):
            temp = temp.next
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
        temp          = self.get(index -1) 
        new_node.next = temp.next
        temp.next     = new_node
        self.length  += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev         = self.get(index -1)
        temp         = prev.next
        prev.next    = temp.next
        temp.next    = None
        self.length -= 1
        return temp
        
    def reverse(self):
        temp      = self.head
        self.head = self.tail
        self.tail = temp
        before    = None
        after     = temp.next
        for _ in range(self.length):
            after     = temp.next
            temp.next = before
            before    = temp
            temp      = after


my_linked_list = LinkedList('D')
my_linked_list.append('C')
my_linked_list.append('B')
my_linked_list.append('C')
my_linked_list.pop()
my_linked_list.prepend('V')
my_linked_list.pop_first()
my_linked_list.set_value(2, 'C')
my_linked_list.insert(3, 'A')
my_linked_list.remove(2)
my_linked_list.insert(2, 'B')
my_linked_list.reverse()
print(my_linked_list.get(1))

my_linked_list.print_list()

'''
#################################################################
#################################################################
#################################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
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
            self.head   = new_node
            self.length = new_node
        else:
            self.tail.next = new_node
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail      = prev
        self.tail.next = None
        self.length   -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp         = self.head
        self.head    = self.head.next
        temp.next    = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
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
        temp          = self.get(index -1)
        new_node.next = temp.next
        temp.next     = new_node
        self.length  += 1
        return temp
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev         = self.get(index -1)
        temp         = prev.next
        prev.next    = temp.next
        temp.next    = None
        self.length -= 1
        return temp

    def reverse(self):
        temp      = self.head
        self.head = self.tail
        self.tail = self.head
        before    = None
        after     = temp.next
        for _ in range(self.length):    # while temp:
            after     = temp.next
            temp.next = before
            before    = temp
            temp      = after



my_linked_list = LinkedList('A')
my_linked_list.append('B')
my_linked_list.append('B')
my_linked_list.pop()
my_linked_list.prepend('Z')
my_linked_list.prepend('X')
my_linked_list.pop_first()
my_linked_list.set_value(1, 'C')
my_linked_list.set_value(0, 'D')
my_linked_list.insert(0, 'E')
my_linked_list.insert(2, 'X')
my_linked_list.insert(5, 'A')
my_linked_list.remove(2)
my_linked_list.reverse()
my_linked_list.print_list()

'''


#################################################################
#################################################################
#################################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
    def __init__(self,value):
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
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail      = prev
        self.tail.next = None
        self.length   -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node            
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp         = self.head
        self.head    = self.head.next
        temp.next    = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
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
        temp          = self.get(index -1)
        new_node.next = temp.next
        temp.next     = new_node
        self.length  += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        prev      = self.get(index -1)
        temp      = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp      = self.head
        self.head = self.tail
        self.tail = temp
        before    = None
        after     = temp.next
        for _ in range(self.length):    # while temp:
            after     = temp.next
            temp.next = before
            before    = temp
            temp      = after


my_linked_list = LinkedList(4)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(4)
my_linked_list.pop()
my_linked_list.pop_first()
my_linked_list.prepend(2)
my_linked_list.insert(0, 1)
my_linked_list.insert(1, 1)
my_linked_list.remove(1)
my_linked_list.reverse()
my_linked_list.print_list()

'''


#################################################################
#################################################################
#################################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
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
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail      = prev
        self.tail.next = None
        self.length   -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        while temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node      = Node(value)
        temp          = self.get(index -1)
        new_node.next = temp.next
        temp.next     = new_node
        self.length  += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop() 

        prev         = self.get(index -1)
        temp         = prev.next
        prev.next    = temp.next
        temp.next    = None
        self.length -= 1
        return temp

    def reverse(self):
        temp      = self.head
        self.head = self.tail
        self.tail = temp
        after     = temp.next
        before    = None

        for _ in range(self.length):
            after     = temp.next
            temp.next = before
            before    = temp
            temp      = after


my_linked_list = LinkedList(9)
my_linked_list.append(8)
my_linked_list.append(7)
my_linked_list.append(7)
my_linked_list.pop()
my_linked_list.prepend(0)
my_linked_list.pop_first()
my_linked_list.set_value(0, 0)
my_linked_list.insert(1, 2)
my_linked_list.remove(2)
my_linked_list.reverse()
my_linked_list.print_list()
#print(my_linked_list.get(0))
'''
#################################################################
#################################################################
#################################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
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
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail      = prev
        self.tail.next = None
        self.length   -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp      = self.head
        self.head = self.head.next
        temp.next = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        while temp:
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
        temp          = self.get(index -1)
        new_node.next = temp.next
        temp.next     = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev         = self.get(index -1)
        temp         = prev.next
        prev.next    = temp.next
        temp.next    = None
        self.length -= 1
        return temp
    
    def reverse(self):
        if self.length <= 1:
            return
        temp      = self.head
        self.head = self.tail
        self.tail = temp
        before    = None
        after     = temp.next
        while temp:
            after     = temp.next
            temp.next = before
            before    = temp
            temp      = after



my_linked_list = LinkedList(3)
my_linked_list.append(2)
my_linked_list.append(0)
my_linked_list.pop()
my_linked_list.prepend('X')
my_linked_list.pop_first()
my_linked_list.set_value(0, 0)
my_linked_list.set_value(1, 1)
my_linked_list.append(2)
my_linked_list.insert(1, 9)
my_linked_list.remove(1)
my_linked_list.reverse()
my_linked_list.print_list()
# print(my_linked_list.get(1))
'''
#################################################################
#################################################################
#################################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
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
            temp = self.head
            prev = self.head
            while temp.next:
                prev = temp
                temp = temp.next
            self.tail = prev
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
            self.head     = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.tail = None
        else:
            temp      = self.head
            self.head = self.head.next
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
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
        temp          = self.get(index -1)
        new_node.next = temp.next
        temp.next     = new_node
        self.length  += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev         = self.get(index -1)
        temp         = prev.next
        prev.next    = temp.next
        temp.next    = None
        self.length -= 1
        return temp

    def reverse(self):
        temp      = self.head
        self.head = self.tail
        self.tail = temp
        after     = temp.next
        before    = None
        for _ in range(self.length):
            after     = temp.next
            temp.next = before
            before    = temp
            temp      = after

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.pop()
my_linked_list.prepend(0)
my_linked_list.pop_first()
my_linked_list.set_value(0, 3)
my_linked_list.insert(1, 4)
my_linked_list.insert(3, 1)
my_linked_list.remove(1)
my_linked_list.reverse()
my_linked_list.print_list()
# print(my_linked_list.get(1))
'''
#################################################################
#################################################################
#################################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
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
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail      = prev
        self.tail.next = None
        self.length   -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp         = self.head
        self.head    = self.head.next
        temp.next    = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
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
        temp          = self.get(index -1)
        new_node.next = temp.next
        temp.next     = new_node
        self.length  += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev        = self.get(index -1)
        temp        = prev.next
        prev.next   = temp.next
        temp.next   = None
        self.length -= 1
        return temp

    def reverse(self):
        if self.length < 2:
            return
        temp      = self.head
        self.head = self.tail
        self.tail = temp
        after     = temp.next
        before    = None
        for _ in range(self.length):
            after     = temp.next
            temp.next = before
            before    = temp
            temp      = after
        
'''

#################################################################
#################################################################
#################################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
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
        print()

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
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
        prev          = self.get(index -1)
        new_node.next = prev.next
        prev.next     = new_node
        self.length  += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev = self.get(index -1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp      = self.head
        self.head = self.tail
        self.tail = temp
        after     = temp.next
        before    = None
        for _ in range(self.length):
            after     = temp.next
            temp.next = before
            before    = temp
            temp      = after

ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.pop()
ll.prepend(0)
ll.pop_first()
ll.set_value(0, 'C')
ll.insert(1, 'B')
ll.insert(1, 'B')
ll.remove(2)
ll.remove(2)
ll.insert(2, 'A')
ll.reverse()
ll.print_list()
'''

#################################################################
#################################################################
#################################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
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
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        if self.length == 0:
            self.head = None
            self.tail = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)    
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        if self.length == 0:
            self.tail = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
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
        temp          = self.get(index -1)
        new_node.next = temp.next
        temp.next     = new_node
        self.length  += 1
        return True 

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        previous = self.get(index -1)
        temp = previous.next
        previous.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
        
    def reverse(self):
        temp      = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        after  = temp.next
        for _ in range(self.length):
            after     = temp.next
            temp.next = before
            before    = temp
            temp      = after
        


ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.pop()
ll.prepend(0)
ll.prepend(0)
ll.pop_first()
ll.set_value(1, 'A')
ll.insert(2, 'B')
ll.remove(2)
ll.reverse()
ll.print_list()
# print(ll.get(1))
'''


#################################################################
#################################################################
#################################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
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
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        if self.length == 0:
            self.head = None
            self.tail = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp      = self.head
        self.head = self.head.next
        temp.next = None
        if self.length == 0:
            self.tail = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        if index < 0 or index > self.length:
            return False
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node      = Node(value)
        temp          = self.get(index -1)
        new_node.next = temp.next
        temp.next     = new_node
        self.length  += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev = self.get(index -1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp      = self.head
        self.head = self.tail
        self.tail = temp

        after  = temp.next
        before = None

        for _ in range(self.length):
            after     = temp.next
            temp.next = before
            before    = temp
            temp      = after


ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.pop()
ll.prepend(0)
ll.prepend(0)
ll.pop_first()
ll.set_value(1, 'X')
ll.insert(1, 'Z')
ll.insert(4, 'O')
ll.remove(3)
ll.reverse()
ll.print_list()
# print(ll.get(1))
'''

#################################################################
#################################################################
#################################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class LinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(f'{temp.value}', end = " ")
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        if self.length == 0:
            self.tail = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
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
        temp     = self.get(index -1)
        new_node.next = temp.next
        temp.next     = new_node
        self.length  += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev = self.get(index -1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        if self.length < 2:
            return
        temp      = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after  = temp.next
        while temp:
            after     = temp.next
            temp.next = before
            before    = temp
            temp      = after



ll = LinkedList(3)
ll.append(2)
ll.append(2)
ll.pop()
ll.prepend(1)
ll.prepend(1)
ll.pop_first()
ll.set_value(1, 0)
ll.insert(3, 3)
ll.remove(1)
ll.reverse()
ll.print_list()
# print(ll.get(1))
'''
#################################################################
#################################################################
#################################################################

class Node:
    def __init__(self, value):
        self.value  = value
        self.next   = None


class LinkedList:
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
            self.tail      = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail      = prev
        self.tail.next = None
        if self.length == 0:
            self.head = None
            self.tail = None
        self.length   -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        if self.length == 0:
            self.tail = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        ...






ll = LinkedList(3)
ll.append(2)
ll.append(1)
ll.pop()
ll.prepend(0)
ll.pop_first()
ll.set_value(0, 'A')
ll.print_list()