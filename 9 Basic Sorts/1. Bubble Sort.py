                # Time complexity: O(n^2) : worst case, if the list is reversed
'''
def bubble_sort(my_list):
    for i in range(len(my_list) -1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list

print(bubble_sort([4, 2, 6, 5, 1, 3]))
'''

#'''
def bs(arr):  # As the first sorted element in the list will be the last one, it                        
    for i in range(len(arr) -1, 0, -1):   # iterates over the list in reverse to
        for j in range(i):          # gradually reduce the elements to be sorted  
            if arr[j] > arr[j + 1]:                                # or compared.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bs([5, 2, 7, 1, 4]))
#'''