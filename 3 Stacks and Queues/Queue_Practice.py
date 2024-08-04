'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class Queue:
    def __init__(self, value):
        new_node    = Node(value)
        self.first  = new_node
        self.last   = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(f'{temp.value}', end = ' ')
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:            # or if not self.first:
            self.first = new_node
            self.last  = new_node
        else:
            self.last.next = new_node
            self.last      = new_node
        self.length += 1
        # return True

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last  = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp
 

my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.dequeue()
my_queue.print_queue()
'''

###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class Queue:
    def __init__(self, value):
        new_node    = Node(value)
        self.first  = new_node
        self.last   = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(f'{temp.value}', end = ' ')
            temp = temp.next
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last  = new_node
        else:
            self.last.next = new_node
            self.last      = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last  = None
        else:
            self.first = self.first.next
            temp.next  = None
        self.length -= 1
        return temp
    
q = Queue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.print_queue()
'''
###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class Queue:
    def __init__(self, value):
        new_node    = Node(value)
        self.first  = new_node
        self.last   = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(f'{temp.value}', end= " ")
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last  = new_node
        else:
            self.last.next = new_node
            self.last      = new_node
        self.length += 1
    
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last  = None
        else:
            self.first = self.first.next
            temp.next  = None
        self.length -= 1
        return temp
            

q = Queue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.print_queue()
'''
###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class Queue:
    def __init__(self, value):
        new_node    = Node(value)
        self.first  = new_node
        self.last   = new_node
        self.length = 1

    def print_q(self):
        temp = self.first
        while temp:
            print(f'{temp.value}', end= " ")
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last  = new_node
        else:
            self.last.next = new_node
            self.last      = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last  = None
        else:
            self.first = self.first.next
            temp.next  = None
        self.length -= 1
        return temp
    
q = Queue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.print_q()
'''
###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last  = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(f'{temp.value}', end= " ")
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if not self.first:
            self.first = new_node
            self.last  = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if not self.first:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last  = None
        self.first = self.first.next
        temp.next = None
        self.length -= 1
        return temp
    
    
q = Queue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.print_queue()

'''

###############################################################
###############################################################
###############################################################
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class Queue:
    def __init__(self, value):
        new_node    = Node(value)
        self.first  = new_node
        self.last   = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(f'{temp.value}', end=" ")
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last  = new_node
        else:
            self.last.next = new_node
            self.last      = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp         = self.first
        self.first   = self.first.next
        temp.next    = None
        self.length -= 1

q = Queue(0)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.print_queue()
'''
###############################################################
###############################################################
###############################################################

class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


class Queue:
    def __init__(self, value):
        new_node    = Node(value)
        self.first  = new_node
        self.last   = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(f'{temp.value}', end=" ")
            temp = temp.next
    
    def enqueue(self, value):
        new_node = Node(value)
        if not self.first:
            self.first = new_node
            self.last  = new_node
        else:
            self.last.next = new_node
            self.last      = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp         = self.first
        if self.length == 1:
            self.first = None
            self.last  = None
        else:
            self.first   = self.first.next
            temp.next    = None
        self.length -= 1
        return temp
    

q = Queue(0)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.print_queue()
