"""
List: Remove Element ( ** Interview Question)
Given a list of integers nums and an integer val, write a function remove_element that removes all occurrences of val in the list in-place and returns the new length of the modified list.

The function should not allocate extra space for another list; instead, it should modify the input list in-place with O(1) extra memory.



Input:

A list of integers nums .

An integer val representing the value to be removed from the list.



Output:

An integer representing the new length of the modified list after removing all occurrences of val.



Constraints:

Do not use any built-in list methods, except for pop() to remove elements.

It is okay to have extra space at the end of the modified list after removing elements.

"""
# WRITE THE REMOVE_ELEMENT FUNCTION HERE #
#                                        #
#                                        #
#                                        #
#                                        #
##########################################
def remove_element(nums, val):
    index = 0
    for _ in range(len(nums)):
        if nums[index] != val:
            index += 1
        else:
            nums.pop(index)
    return index



# Test case 1: Removing a single instance of a value (1) in the middle of the list.
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
val1 = 1
print("\nRemove a single instance of value", val1, "in the middle of the list.")
print("BEFORE:", nums1)
new_length1 = remove_element(nums1, val1)
print("AFTER:", nums1, "\nNew length:", new_length1)
print("-----------------------------------")

# Test case 2: Removing a value that's located at the end of the list.
nums2 = [1, 2, 3, 4, 5, 6]
val2 = 6
print("\nRemove value", val2, "that's located at the end of the list.")
print("BEFORE:", nums2)
new_length2 = remove_element(nums2, val2)
print("AFTER:", nums2, "\nNew length:", new_length2)
print("-----------------------------------")

# Test case 3: Removing a value that's located at the start of the list.
nums3 = [-1, -2, -3, -4, -5]
val3 = -1
print("\nRemove value", val3, "that's located at the start of the list.")
print("BEFORE:", nums3)
new_length3 = remove_element(nums3, val3)
print("AFTER:", nums3, "\nNew length:", new_length3)
print("-----------------------------------")

# Test case 4: Attempting to remove a value from an empty list.
nums4 = []
val4 = 1
print("\nAttempt to remove value", val4, "from an empty list.")
print("BEFORE:", nums4)
new_length4 = remove_element(nums4, val4)
print("AFTER:", nums4, "\nNew length:", new_length4)
print("-----------------------------------")

# Test case 5: Removing all instances of a repeated value.
nums5 = [1, 1, 1, 1, 1]
val5 = 1
print("\nRemove all instances of value", val5, "from the list.")
print("BEFORE:", nums5)
new_length5 = remove_element(nums5, val5)
print("AFTER:", nums5, "\nNew length:", new_length5)
print("-----------------------------------")

"""
HINTS:

Pseudo Code:

function remove_element(array, value)

    initialize index i to 0

    while iterating through the array

        if current element equals the value

            remove the current element from the array

        else

            move to the next element

    return the length of the modified array
"""

"""
SOLUTION:

def remove_element(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)




The logic of the remove_element function is to iterate through the input array nums and remove all instances of the given value val. Here's a step-by-step explanation of the code:



Initialize an index variable i to 0, which will be used to traverse the nums array.

Use a while loop to iterate through the array until i reaches the end of the array (i < len(nums)).

Inside the loop, check if the current element at index i is equal to the given value val.

If the current element is equal to val, remove it from the array using the pop() method. Note that this operation modifies the array in-place. Since the current element was removed, the next element will take its place, so the index i does not need to be incremented in this case.

If the current element is not equal to val, increment the index i by 1, moving on to the next element in the array.

The loop continues until all elements in the array have been checked.

After the loop is finished, return the new length of the modified array using len(nums).





Code with inline comments:



def remove_element(nums, val):
    # Initialize the index variable to 0
    i = 0
    
    # Iterate through the array using a while loop
    while i < len(nums):
        # Check if the current element is equal to the given value
        if nums[i] == val:
            # If equal, remove the element in-place using pop()
            nums.pop(i)
        else:
            # If not equal, increment the index to move to the next element
            i += 1
    
    # Return the new length of the modified array
    return len(nums)
"""