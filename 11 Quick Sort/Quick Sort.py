#                     \('=.=)_/ QUICK|<->:<->|SORT \_(=.=')/
#                       
#              Time complexity: O(n log n) for best & average case
#                               worst case O(n^2) -- if the list is already sorted                          
#

'''
def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


my_list = [4, 6, 1, 7, 3,  2, 5]
print(pivot(my_list, 0, 6)) # swap_index
print(my_list)              


def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index + 1, right)
    return my_list


def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)

print(quick_sort([4, 6, 1, 7, 3, 2, 5]))
'''


'''
def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index + 1, right)
    return my_list    

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)


print(quick_sort([4, 6, 1, 7, 3, 2, 5]))
'''


'''
def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index + 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return pivot_index

def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index + 1, right)
    return my_list


def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)


print(quick_sort([4, 6, 1, 7, 3, 2, 5]))
'''


'''
def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index + 1, right)
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)


print(quick_sort([4, 6, 1, 7, 3, 2, 5]))
'''


'''
def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index   # which is where the pivot_index ended


def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index + 1, right)
    return my_list


def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)



print(quick_sort([4, 6, 1, 7, 3, 2, 5]))
'''


'''
def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index + 1, right)
    return my_list


def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)


print(quick_sort([4, 6, 1, 7, 3, 2, 5]))
'''


'''
def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

    
def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

    
def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index -1)
        quick_sort_helper(my_list, pivot_index +1, right)
    return my_list

    
def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) -1)


print(quick_sort([4, 6, 1, 7, 3, 2, 5]))
'''


'''
def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index +1, end_index +1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index -1)
        quick_sort_helper(my_list, pivot_index +1, right)
    return my_list


def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) -1)


print(quick_sort([4, 6, 1, 7, 3, 2, 5]))
'''


#'''
def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] =\
    my_list[index2], my_list[index1]


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index + 1, right)
    return my_list


def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)



print(quick_sort([4, 6, 1, 7, 3, 2, 5]))
#'''