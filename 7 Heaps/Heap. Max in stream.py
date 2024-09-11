"""
Heap: Maximum Element in a Stream

Write a function named stream_max that takes as 
its input a list of integers (nums). 
The function should return a list of the same length, 
where each element in the output list is the maximum 
number seen so far in the input list.

More specifically, for each index i in the input list, 
the element at the same index in the output list 
should be the maximum value among the elements at 
indices 0 through i in the input list.

Use the provided MaxHeap class to solve this problem. You should not need to modify the MaxHeap class to complete this task.

Function Signature: def stream_max(nums):


Examples:

If the input list is [1, 3, 2, 5, 4], the function 
should return [1, 3, 3, 5, 5].

Explanation:

At index 0, the maximum number seen so far is 1.

At index 1, the maximum number seen so far is 3.

At index 2, the maximum number seen so far is still 3.

At index 3, the maximum number seen so far is 5.

At index 4, the maximum number seen so far is still 5.

So, the output list is [1, 3, 3, 5, 5].

Similarly, if the input list is [7, 2, 4, 6, 1], 
the function should return [7, 7, 7, 7, 7].

Explanation:

At each index, the maximum number seen so far is 7.

So, the output list is [7, 7, 7, 7, 7].


Constraints:

You may assume that the input list does not contain 
any null or undefined elements.
"""

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

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
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value
        


###### WRITE STREAM_MAX FUNCTION HERE ######
#                                          #
#   This is a separate function that is    #
#   not a method within the Heap class.    #
#   Indent all the way to the left.        #
#                                          #
############################################
def stream_max(nums):
    my_heap = MaxHeap()
    stream = []

    for num in nums:
        my_heap.insert(num)
        stream.append(my_heap.heap[0])
    
    return stream



test_cases = [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 2, 2, 1, 3, 3, 3, 2, 2], [1, 2, 2, 2, 3, 3, 3, 3, 3]),
    ([-1, -2, -3, -4, -5], [-1, -1, -1, -1, -1])
]

for i, (nums, expected) in enumerate(test_cases):
    result = stream_max(nums)
    print(f'\nTest {i+1}')
    print(f'Input: {nums}')
    print(f'Expected Output: {expected}')
    print(f'Actual Output: {result}')
    if result == expected:
        print('Status: Passed')
    else:
        print('Status: Failed')



"""
    EXPECTED OUTPUT:
    ----------------
    Test 1
    Input: []
    Expected Output: []
    Actual Output: []
    Status: Passed
    Test 2
    Input: [1]
    Expected Output: [1]
    Actual Output: [1]
    Status: Passed
    Test 3
    Input: [1, 2, 3, 4, 5]
    Expected Output: [1, 2, 3, 4, 5]
    Actual Output: [1, 2, 3, 4, 5]
    Status: Passed
    Test 4
    Input: [1, 2, 2, 1, 3, 3, 3, 2, 2]
    Expected Output: [1, 2, 2, 2, 3, 3, 3, 3, 3]
    Actual Output: [1, 2, 2, 2, 3, 3, 3, 3, 3]
    Status: Passed
    Test 5
    Input: [-1, -2, -3, -4, -5]
    Expected Output: [-1, -1, -1, -1, -1]
    Actual Output: [-1, -1, -1, -1, -1]
    Status: Passed

"""

'''
MY FIRST SOLUTION:


    build = MaxHeap()
    output = []

    for num in nums:
        build.insert(num)
        if build.heap[0] > num:
            output.append(build.heap[0])
        else:
            output.append(num)
    return output

#################################################
    
    ORIGINAL SOLUTION:

def stream_max(nums):
    max_heap = MaxHeap()
    max_stream = []
 
    for num in nums:
        max_heap.insert(num)
        max_stream.append(max_heap.heap[0])
 
    return max_stream
'''

"""
Pseudo Code:



Initialize an empty MaxHeap.

This will be used to keep track of the maximum number seen so far.

Initialize an empty list, max_stream.

This will be used to store the maximum numbers encountered at 
each position in the input list.

Start a loop that iterates over each number in the input list.

For each iteration (i.e., for each number in the input list):

Insert the current number into the MaxHeap.

The heap will reorganize itself such that the maximum number 
is always at the root.

Append the value at the root of the heap (i.e., the maximum 
number so far) to the max_stream list.

After all numbers from the input list have been processed, 
return the max_stream list.

This list represents the maximum number encountered so far at 
each position in the input list.





Explained another way:

Imagine you are playing a game with your friends. 
The game is about guessing the biggest number any of you have 
thought of so far. You all sit in a circle and start saying 
numbers one by one.

You need a strategy to always remember the biggest number any 
of your friends has said. So, you decide to use a special box, 
which you'll call a "MaxHeap". Every time one of your friends 
says a number, you put it into this box.

The magic about this box is that it always arranges the numbers 
in a way that the biggest number always jumps to the top of the 
box, so you can easily see it.

After every turn (each friend saying a number), you write down 
the number at the top of the box on a piece of paper.

At the end of the game, you'll have a list of numbers on your 
paper. Each of these numbers is the biggest number that was said 
up to that point in the game.

That's what the stream_max function does. It uses a "MaxHeap" 
box (which is just a fancy name for a special kind of list) to 
always keep track of the biggest number it has seen, and it 
writes that number down after each turn. When it's done going 
through all the numbers, it gives you the piece of paper with 
the list of biggest numbers it has written down.

"""

"""
The stream_max function takes as input a list of numbers (nums) 
and returns a list of the maximum numbers encountered so far in 
the input list. It achieves this using a MaxHeap data structure.

Here's a breakdown of the function:

max_heap = MaxHeap(): This line creates an empty MaxHeap. 
In a MaxHeap, the parent node is always larger than or equal to its child nodes. In this case, we use the MaxHeap to easily keep track of the maximum value encountered so far.

max_stream = []: This line initializes an empty list which will eventually store the maximum numbers encountered so far.

for num in nums:: This line starts a loop that iterates over each number in the input list nums.

max_heap.insert(num): For each number, it is inserted into the MaxHeap. If the number is greater than the current maximum number in the heap, the heap adjusts itself so that this number moves to the root position (i.e., it becomes the new maximum).

max_stream.append(max_heap.heap[0]): After each insertion, the maximum value in the heap (which is always at the root, and can be accessed using max_heap.heap[0]) is appended to the max_stream list. This means max_stream[i] will always be the maximum value in nums up to index i.

return max_stream: Finally, after the loop is done, the max_stream list is returned. This list represents the maximum number encountered so far for each position in the input list.



For example, if nums = [1, 3, 2, 5, 4], then stream_max(nums) would return [1, 3, 3, 5, 5] because at each position, those are the maximum numbers encountered so far.





Code with inline comments:



def stream_max(nums):
    # Initialize an empty MaxHeap.
    # This is a data structure where the parent node
    # is always larger than or equal to its children.
    max_heap = MaxHeap()
    
    # Initialize an empty list to store the maximum numbers 
    # encountered so far while traversing the input list.
    max_stream = []
 
    # Iterate over each number in the input list.
    for num in nums:
        # Insert the current number into the MaxHeap.
        # If this number is greater than the current maximum
        # number in the heap, the heap will adjust itself
        # so that this number becomes the new maximum
        # (i.e., it moves to the root of the heap).
        max_heap.insert(num)
        
        # After each insertion, append the maximum value in the heap
        # to the max_stream list. This value is always at the root
        # of the heap and can be accessed using max_heap.heap[0].
        # As a result, max_stream[i] will always be the maximum value
        # in nums up to index i.
        max_stream.append(max_heap.heap[0])
 
    # After we've finished the loop, return the max_stream list.
    # This list represents the maximum number encountered so far 
    # for each position in the input list.
    return max_stream
 
"""