#       Merge Sort     Time Complexity: O(n log n) | Space complexity: O(n)
#                    (log n) for dividing the array and (n) for putting it back

'''
def merge(list1, list2):
    combined = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2): # run until one of the lists is empty
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


# print(merge([1, 2, 7, 8], [3, 4, 5, 6])) # test the merge helper function


def merge_sort(my_list):
    if len(my_list) == 1: return my_list    # base case for recurrsion
    mid_index = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid_index])  # start to mid_index (not included)
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)


print(merge_sort([3, 1, 4, 2]))
'''


'''
def merge(list1, list2):
    combined = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


def merge_sort(my_list):
    if len(my_list) == 1: return my_list
    mid_index = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])
    return merge(left, right)


print(merge_sort([3, 5, 1, 0, 8]))
'''


'''
def merge(list1, list2):
    combined = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


def merge_sort(my_list):
    if len(my_list) == 1: return my_list
    mid_index = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])
    return merge(left, right)


print(merge_sort([3, 5, 1, 0, 8]))
'''


'''
def merge(list1, list2):
    combined = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])
    return merge(left, right)

 
print(merge_sort([3, 5, 1, 0, 8]))
'''

#'''
def merge(list1, list2):
    combined = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])        
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


def merge_sort(my_list):
    if len(my_list) == 1: return my_list
    mid_index = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])
    return merge(left, right)


print(merge_sort([3, 5, 1, 0, 8]))
#'''