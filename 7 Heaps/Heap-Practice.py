
'''
class MaxHeap:
    def __init__(self):
        self.heap = []


    def _left_child(self, index):
        return 2 * index + 1 # we use the 0 index for the max value
    

    def _right_child(self, index):
        return 2 * index + 2
    

    def _parent(self, index):
        return (index - 1) // 2
    

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = \
            self.heap[index2], self.heap[index1]

    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and \
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


my_heap = MaxHeap()
my_heap.insert(99)
my_heap.insert(72)
my_heap.insert(61)
my_heap.insert(58)    
print(my_heap.heap)

my_heap.insert(100)
print(my_heap.heap)

my_heap.insert(75)
print(my_heap.heap)

'''
#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []


    def _left_child(self, index):
        return index * 2 + 1
    

    def _right_child(self, index):
        return index * 2 + 2
    

    def _parent(self, index):
        return (index - 1) // 2
    

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = \
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1  # tracks the current index        

        while current > 0 and \
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)




my_heap = MaxHeap()
my_heap.insert(99)
my_heap.insert(72)
my_heap.insert(61)
my_heap.insert(58)    
print(my_heap.heap)

my_heap.insert(100)
print(my_heap.heap)

my_heap.insert(75)
print(my_heap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []


    def _left_child(self, index):
        return index * 2 + 1
        

    def _right_child(self, index): 
        return index * 2 + 2


    def _parent(self, index):
        return (index - 1) // 2
    

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = \
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and \
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)



my_heap = MaxHeap()
my_heap.insert(99)
my_heap.insert(72)
my_heap.insert(61)
my_heap.insert(58)    
print(my_heap.heap)

my_heap.insert(100)
print(my_heap.heap)

my_heap.insert(75)
print(my_heap.heap)

'''

#################################################################
#################################################################
#################################################################

'''

class MaxHeap:
    def __init__(self):
        self.heap = []


    def _left_child(self, index):
        return index * 2 + 1
    

    def _right_child(self, index):
        return index * 2 + 2


    def _parent(self, index):
        return (index - 1) // 2
    

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = \
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and \
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)



my_heap = MaxHeap()
my_heap.insert(99)
my_heap.insert(72)
my_heap.insert(61)
my_heap.insert(58)    
print(my_heap.heap)

my_heap.insert(100)
print(my_heap.heap)

my_heap.insert(75)
print(my_heap.heap)

'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []


    def _left_child(self, index):
        return index * 2 + 1
    

    def _right_child(self, index):
        return index * 2 + 2
    

    def _parent(self, index):
        return (index - 1) // 2
    

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = \
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and \
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)



my_heap = MaxHeap()
my_heap.insert(99)
my_heap.insert(72)
my_heap.insert(61)
my_heap.insert(58)    
print(my_heap.heap)

my_heap.insert(100)
print(my_heap.heap)

my_heap.insert(75)
print(my_heap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []


    def _left_child(self, index):
        return index * 2 + 1
    

    def _right_child(self, index):
        return index * 2 + 2
    

    def _parent(self, index):
        return (index - 1) // 2
    

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = \
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and \
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)



my_heap = MaxHeap()
my_heap.insert(99)
my_heap.insert(72)
my_heap.insert(61)
my_heap.insert(58)    
print(my_heap.heap)

my_heap.insert(100)
print(my_heap.heap)

my_heap.insert(75)
print(my_heap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []


    def _left_child(self, index):
        return index * 2 + 1
    

    def _right_child(self, index):
        return index * 2 + 2
    

    def _parent(self, index):
        return (index - 1) // 2
    

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = \
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and \
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)



my_heap = MaxHeap()
my_heap.insert(99)
my_heap.insert(72)
my_heap.insert(61)
my_heap.insert(58)    
print(my_heap.heap)

my_heap.insert(100)
print(my_heap.heap)

my_heap.insert(75)
print(my_heap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []


    def _left_child(self, index):
        return index * 2 + 1


    def _right_child(self, index):
        return index * 2 + 2


    def _parent(self, index):
        return (index - 1) // 2
    

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = \
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and \
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)            
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and
                self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and
                self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return


    def remove(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value
    



my_heap = MaxHeap()
my_heap.insert(99)
my_heap.insert(72)
my_heap.insert(61)
my_heap.insert(58)    
my_heap.insert(100)
print(my_heap.heap)
my_heap.remove()
my_heap.insert(75)
print(my_heap.heap)
my_heap.remove()
print(my_heap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []


    def _left_child(self, index):
        return index * 2 + 1
    

    def _right_child(self, index):
        return index * 2 + 2
    

    def _parent(self, index):
        return (index - 1) // 2
    

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = \
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and \
            self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and \
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if right_index < len(self.heap) and \
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)

        return max_value


    
myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1 ,index2):
        self.heap[index1], self.heap[index2] = \
        self.heap[index2], self.heap[index1]

    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and \
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    
    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and \
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if right_index < len(self.heap) and \
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)

        return max_value



myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = \
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and \
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
    

    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and \
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if right_index < len(self.heap) and \
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value



myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = \
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and \
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
        

    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and \
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if right_index < len(self.heap) and \
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return 
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value



myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]
    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and \
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    
    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and \
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if right_index < len(self.heap) and \
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value



myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)

'''
#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    
    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index) 

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value
        


myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


    def _sink_down(self, index):
        maxIndex = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[maxIndex]:
                maxIndex = left_index

            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[maxIndex]:
                maxIndex = right_index

            if maxIndex != index:
                self._swap(index, maxIndex)
                index = maxIndex
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        maxValue = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return maxValue
    

            

myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        
        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current) 
    

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value




myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value
    


myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]

    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return


    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value



myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value



myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
    

    def _sink_down(self, index):
        maxIndex = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[maxIndex]:
                maxIndex = left_index

            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[maxIndex]:
                maxIndex = right_index

            if maxIndex != index:
                self._swap(index, maxIndex)
                index = maxIndex
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        maxValue = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return maxValue



myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2): 
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


    def _sink_down(self, index):
        maxIndex = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[maxIndex]:
                maxIndex = left_index

            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[maxIndex]:
                maxIndex = right_index

            if maxIndex != index:
                self._swap(index, maxIndex)
                index = maxIndex
            else:
                return
            
        
    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        maxValue = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return maxValue



myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
            self.heap[index2], self.heap[index1]

    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop() # to maintain index 0

        self._sink_down(0)
        return max_value




myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    
    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value
    


myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []


    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]

    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current)) 
            current = self._parent(current)


    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return


    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]       
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value



myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []


    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]

    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value



myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []
    

    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]

        
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        if current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
    

    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            
    
    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value
    

myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []


    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1] 


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        if current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
    

    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)    
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value




myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []


    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
    

    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value



myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []


    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value


            
myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []


    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
    

    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
                
    
    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value
    

                
myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []


    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value



myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    
    def _left_child(self, index): return index * 2 + 1

    def _right_child(self, index): return index * 2 + 2

    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value



myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []


    def _left_child(self, index): return index * 2 + 1
    def _right_child(self, index): return index * 2 + 2
    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]

    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
    

    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()        

        self._sink_down(0)
        return max_value



myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)

'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []


    def _left_child(self, index): return index * 2 + 1
    def _right_child(self, index): return index * 2 + 2
    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current)) #changes the  value
            current = self._parent(current)            #changes the index


    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value
    



myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    
    def _left_child(self, index): return index * 2 + 1
    def _right_child(self, index): return index * 2 + 2
    def _parent(self, index): return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]

    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
        

    def _sink_down(self, index):
       max_index = index
       
       while True:
           left_index = self._left_child(index) 
           right_index = self._right_child(index)

           if left_index < len(self.heap) and\
           self.heap[left_index] > self.heap[max_index]:
               max_index = left_index
           if right_index < len(self.heap) and\
           self.heap[right_index] > self.heap[max_index]:
               max_index = right_index

           if max_index != index:
               self._swap(index, max_index)
               index = max_index
           else:
               return


    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value
    


myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []
    

    def _left_child(self, index): return index * 2 + 1
    def _right_child(self, index): return index * 2 + 2
    def _parent(self, index): return (index - 1) // 2


    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]

    
    def insert(self, value):
        self.heap.append(value)  
        current = len(self.heap) - 1
        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
        

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            
            if (left_index < len(self.heap) and
            self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and
            self.heap[right_index] > self.heap[max_index]):
                max_index = right_index
            
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return


    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop() # moving the last value up

        self._sink_down(0) # start comparing from the root
        return max_value



myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []
    

    def _left_child(self, index): return index * 2 + 1
    def _right_child(self, index): return index * 2 + 2
    def _parent(self, index): return (index - 1) // 2


    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]

    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) -1
        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
    

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            
            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            
            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value
    



myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    
    def _left_child(self, index): return index * 2 + 1
    def _right_child(self, index): return index * 2 + 2
    def _parent(self, index): return (index - 1) // 2


    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]
        

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) -1
        
        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
        

    def _sink_down(self, index):
        max_index = index
        while True:
            left_child = self._left_child(index)
            right_child = self._right_child(index)

            if left_child < len(self.heap) and\
            self.heap[left_child] > self.heap[max_index]:
                max_index = left_child
            
            if right_child < len(self.heap) and\
            self.heap[right_child] > self.heap[max_index]:
                max_index = right_child

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            
    
    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value
    


myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

'''
class MaxHeap:
    def __init__(self):
        self.heap = []
    

    def _left_child(self, index): return index * 2 + 1
    def _right_child(self, index): return index * 2 + 2
    def _parent(self, index): return (index - 1) // 2


    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
        self.heap[index2], self.heap[index1]

    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) -1

        while current > 0 and\
        self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
    

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
            self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            
            if right_index < len(self.heap) and\
            self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            

    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return max_value
    


myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
'''

#################################################################
#################################################################
#################################################################

#'''
class MaxHeap:
    def __init__(self):
        self.heap = []
    

    def _left_child(self, index): return index * 2 + 1
    def _right_child(self, index): return index * 2 + 2
    def _parent(self, index): return (index - 1) // 2


    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =\
            self.heap[index2], self.heap[index1]
    

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) -1
        while current > 0 and\
            self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and\
                self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and\
                self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return


    def remove(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop() # takes the last element
# and moves it at the top to keep the validity of the heap    
        self._sink_down(0)
        return max_value


myHeap = MaxHeap()
myHeap.insert(12)
myHeap.insert(23)
myHeap.insert(44)
myHeap.insert(17)
myHeap.insert(31)
myHeap.insert(88)
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)
#'''

#################################################################
#################################################################
#################################################################