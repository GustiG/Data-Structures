"""
List: Remove Duplicates ( ** Interview Question)
Given a sorted list of integers, rearrange the list in-place such that all unique elements appear at the beginning of the list.

Your function should return the new length of the list containing only unique elements. Note that you should not create a new list or use any additional data structures to solve this problem. The original list should be modified in-place.

Constraints:



The input list is sorted in non-decreasing order.

The input list may contain duplicates.

The function should have a time complexity of O(n), where n is the length of the input list.

The function should have a space complexity of O(1), i.e., it should not use any additional data structures or create new lists (this also means you cannot use a set like we did earlier in the course).



Example:

Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] Function call: new_length = remove_duplicates(nums) Output: new_length = 5 Modified list: nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4] (first 5 elements are unique)

Explanation: The function modifies the original list nums in-place, moving unique elements to the beginning of the list, followed by duplicate elements. The new length returned by the function is 5, indicating that there are 5 unique elements in the list. The first 5 elements of the modified list nums are the unique elements [0, 1, 2, 3, 4].



This code:



nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = remove_duplicates(nums)
print("New length:", new_length)
print("Unique values in list:", nums[:new_length])


Should Output:



New length: 5
Unique values in list: [0, 1, 2, 3, 4]

"""
# WRITE REMOVE_DUPLICATES FUNCTION HERE #
#                                       #
#                                       #
#                                       #
#                                       #
#########################################
def remove_duplicates(nums):
    if len(nums) == 0: return 0
    index = 1
    for num in range(1, len(nums)):
        if nums[num] != nums[num - 1]:
            nums[index] = nums[num]
            index += 1
    return index
    


# Test case 1: Empty list
test1 = []
print(f"Test 1 Before: {test1}")
result1 = remove_duplicates(test1)
print(f"Test 1 After: {test1[:result1]}")
print(f"New Length: {result1}")
print("------")

# Test case 2: List with all duplicates
test2 = [1, 1, 1, 1, 1]
print(f"Test 2 Before: {test2}")
result2 = remove_duplicates(test2)
print(f"Test 2 After: {test2[:result2]}")
print(f"New Length: {result2}")
print("------")

# Test case 3: List with no duplicates
test3 = [1, 2, 3, 4, 5]
print(f"Test 3 Before: {test3}")
result3 = remove_duplicates(test3)
print(f"Test 3 After: {test3[:result3]}")
print(f"New Length: {result3}")
print("------")

# Test case 4: List with some duplicates
test4 = [1, 1, 2, 2, 3, 4, 5, 5]
print(f"Test 4 Before: {test4}")
result4 = remove_duplicates(test4)
print(f"Test 4 After: {test4[:result4]}")
print(f"New Length: {result4}")
print("------")


"""
SOLUTION:

def remove_duplicates(nums):
    if not nums:
        return 0
 
    write_pointer = 1
 
    for read_pointer in range(1, len(nums)):
        if nums[read_pointer] != nums[read_pointer - 1]:
            nums[write_pointer] = nums[read_pointer]
            write_pointer += 1
 
    return write_pointer




This code defines a function remove_duplicates that takes a sorted list of integers called nums as input and rearranges it in-place to move unique elements to the beginning, followed by duplicate elements. The function returns the new length of the list containing only unique elements.

Here's a step-by-step explanation of the code:



if not nums: return 0: This line checks if the input list nums is empty. If it is, the function returns 0, as there are no unique elements in an empty list.

write_pointer = 1: This line initializes the write_pointer variable with a value of 1. The write_pointer will be used to keep track of the position where the next unique element should be written in the list.

for read_pointer in range(1, len(nums)):: This line starts a for loop that iterates through the list from index 1 to the end of the list. The loop uses the read_pointer variable to track the current position in the list.

if nums[read_pointer] != nums[read_pointer - 1]:: This line checks if the current element at the read_pointer index is different from the previous element. If it is, it means that the current element is unique and should be moved to the position indicated by the write_pointer.

nums[write_pointer] = nums[read_pointer]: This line moves the unique element at the read_pointer index to the position indicated by the write_pointer.

write_pointer += 1: This line increments the write_pointer by 1 to prepare for the next unique element.

return write_pointer: After the loop finishes, the write_pointer variable holds the new length of the list containing unique elements. The function returns this value.



By using the write_pointer and read_pointer variables, the function efficiently modifies the original list in-place without using any additional data structures or creating new lists. It moves unique elements to the beginning of the list and returns the new length of the list containing only unique elements.





Code with inline comments:



def remove_duplicates(nums):
    # Return 0 if input list is empty
    if not nums:
        return 0
 
    # Initialize write_pointer at index 1
    write_pointer = 1
 
    # Loop through list starting from index 1
    for read_pointer in range(1, len(nums)):
        # Check if current element is unique
        if nums[read_pointer] != nums[read_pointer - 1]:
            # Move unique element to write_pointer
            nums[write_pointer] = nums[read_pointer]
            # Increment write_pointer for next unique element
            write_pointer += 1
 
    # Return new length of list with unique elements
    return write_pointer

"""