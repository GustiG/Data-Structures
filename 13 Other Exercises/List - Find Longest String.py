"""
List: Find Longest String ( ** Interview Question)
Write a Python function called find_longest_string that takes a list of strings as an input and returns the longest string in the list. The function should iterate through each string in the list, check its length, and keep track of the longest string seen so far. Once it has looped through all the strings, the function should return the longest string found.



Example:

string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  # expected output: 'banana'
"""
# WRITE FIND_LONGEST_STRING FUNCTION HERE #
#                                         #
#                                         #
#                                         #
#                                         #
###########################################
def find_longest_string(strings):
    max_string = ""
    for string in strings:
        if len(string) > len(max_string):
            max_string = string
    return max_string


string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""

"""
def find_longest_string(string_list):
    longest_string = ""
    for string in string_list:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string




This code defines a function called find_longest_string that takes a single argument string_list, which is expected to be a list of strings.

The function initializes a variable called longest_string to an empty string. Then, it iterates over each string in string_list using a for loop. For each string, the function checks if its length is greater than the length of longest_string using the len function. If the length of the current string is greater than the length of longest_string, then the value of longest_string is updated to be the current string.

After iterating over all the strings in string_list, the function returns longest_string, which will be the string in the list with the greatest length.





Code with inline comments:



def find_longest_string(string_list):
    # Initialize the variable to store the longest string to an empty string
    longest_string = ""
    # Loop through each string in the list of strings
    for string in string_list:
        # Check if the length of the current string is greater than the
        # length of the current longest string
        if len(string) > len(longest_string):
            # If so, update the longest string to be the current string
            longest_string = string
    # Return the longest string
    return longest_string
"""