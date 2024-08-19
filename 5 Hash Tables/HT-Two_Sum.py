"""
HT: Two Sum ( ** Interview Question)
two_sum()

Problem:
Given an array of integers 'nums' and a target integer 'target', 
find the indices of two numbers in the array that add up to 
the target.

The main challenge here is to implement this function in one 
pass through the array. This means you should not iterate over 
the array more than once. Therefore, your solution should have 
a time complexity of O(n), where n is the number of elements 
in nums.



Input:

A list of integers nums .

A target integer target.



Output:

A list of two integers representing the indices of the two 
numbers in the input array nums that add up to the target. 
If no two numbers in the input array add up to the target, 
return an empty list [].



Example:



Input: nums = [5, 1, 7, 2, 9, 3], target = 10
Output: [1, 4]
Explanation: The numbers at indices 1 and 4 in the array add 
up to the target 10.
 
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: The numbers at indices 1 and 2 in the array add 
up to the target 6.
 
Input: nums = [3, 3], target = 6
Output: [0, 1]
Explanation: The numbers at indices 0 and 1 in the array add 
up to the target 6.
 
Input: nums = [2, 1, 2, 7, 11, 15], target = 9
Output: [2, 3]
Explanation: Notice there are two 2s in the array.  
The second one will be used.
 
Input: nums = [1, 2, 3, 4, 5], target = 10
Output: []
Explanation: There are no two numbers in the array add up to 
the target 10.
 
Input: nums = [], target = 0
Output: []
Explanation: There are no numbers in the input array, 
so the function returns an empty list [].

"""

# WRITE TWO_SUM FUNCTION HERE #
#                             #
#                             #
#                             #
#                             #
###############################
def two_sum(nums, target):
    index_value = {}
    for i, num in enumerate(nums):
        result = target - num
        if result in index_value:
            return [index_value[result], i]
        else:
            index_value[num] = i
    return []



print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))  
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
print(two_sum([1, 3, 5, 7, 9], 10))  
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 4]
    [1, 3]
    [0, 3]
    [1, 3]
    []
    [2, 3]
    [0, 1]
    []

"""

'''
Pseudo Code:

Start the function two_sum with two parameters: 
a list nums and an integer target.

Initialize an empty dictionary num_map. 
This will be used to store each number from the list nums 
as a key and its corresponding index as a value.

Begin a loop over the list nums using the enumerate function, 
which provides both the index and the value for each element in 
the list.

3.1. For each element, calculate its "complement" by subtracting 
the current number from the target. 
This is the number we need to find in our dictionary to know 
that the current number and its complement add up to the target.

3.2. Check if the complement is present as a key in the dictionary 
num_map.

3.2.1. If the complement is found, it means we have found two 
numbers that add up to target. Return a list with two elements: 
the value associated with the complement in the dictionary 
num_map (which is the index of the complement in the original list),
and the current index.

3.3. If the complement is not found in the dictionary, 
add the current number to num_map with its index as the value. 
This updates our dictionary to reflect the numbers we have seen 
so far and their corresponding indices.

If the loop finishes without finding two numbers that add up to 
target, return an empty list. 
This means no such pair of numbers exists in the list.
'''

"""
SOLUTION:


def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []


"""


"""
MY first SOLUTION only returns the values, not indexes as required:

    table = {}
    current = 0

    for i in nums:
        current = i
        result = target - current
        if result in table:
            return i, table.get(result)
        else:
            table[i] = current  # or = i
    return []

"""

"""
SOLUTION WITH COMMENTS:

    h_table = {}            # key = num : value = num[index]
    for i, current in enumerate(nums):  # get both index and value
        result = target - current       # find the missing value
        if result in h_table:           # if the value is present
            return [h_table[result], i] # return it's index
        else:
            h_table[current] = i       # add the index to the table
    return [] # return an empty list when the target isn't matched 

"""