"""
List: Find Max Min ( ** Interview Question)
Write a Python function that takes a list of integers as input and returns a tuple containing the maximum and minimum values in the list.

The function should have the following signature:

def find_max_min(myList):


Where myList is the list of integers to search for the maximum and minimum values.

The function should traverse the list and keep track of the current maximum and minimum values. It should then return these values as a tuple, with the maximum value as the first element and the minimum value as the second element.

For example, if the input list is [5, 3, 8, 1, 6, 9], the function should return (9, 1) since 9 is the maximum value and 1 is the minimum value.
"""
# WRITE FIND_MAX_MIN FUNCTION HERE #
#                                  #
#                                  #
#                                  #
#                                  #
####################################
def find_max_min(my_list):
    min_num = max_num = my_list[0]
    for num in my_list:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    return (max_num, min_num)


print( find_max_min([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""

"""
def find_max_min(myList):
    maximum = minimum = myList[0]
    for num in myList:
        if num > maximum:
            maximum = num
        elif num < minimum:
            minimum = num
    return maximum, minimum




This code defines a function called find_max_min, which takes a single argument, myList. The function is designed to find the maximum and minimum values in the given list and return them as a tuple (maximum, minimum). Here's an explanation of the code:



maximum = minimum = myList[0]: This line initializes both the maximum and minimum variables with the value of the first element in the list. This is done as a starting point for comparison with the rest of the elements in the list.

for num in myList:: This line starts a for loop, iterating through each element (num) in the list myList.

if num > maximum:: This line checks if the current element (num) is greater than the current maximum value. If this condition is true, it means we found a new maximum value in the list.

maximum = num: If the condition in the previous line is true, this line assigns the current element's value to the maximum variable, updating it to the new maximum value.

elif num < minimum:: If the current element is not greater than the current maximum, this line checks if the current element is less than the current minimum value. If this condition is true, it means we found a new minimum value in the list.

minimum = num: If the condition in the previous line is true, this line assigns the current element's value to the minimum variable, updating it to the new minimum value.

return maximum, minimum: This line returns a tuple containing the maximum and minimum values found in the list.





Code with inline comments:



def find_max_min(myList):
    # Initialize the maximum and minimum variables 
    # to the first element of the list
    maximum = minimum = myList[0]
    
    # Traverse the list and update the 
    # maximum and minimum variables
    for num in myList:
        if num > maximum:
            maximum = num
        elif num < minimum:
            minimum = num
    
    # Return the maximum and minimum variables
    return maximum, minimum

"""