'''
def selection_sort(my_list):
    for i in range(len(my_list) -1):
        min_index = i
        for j in range(i + 1, len(my_list)):#compare from i+1 up to the index of 5
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:             # if i and min_index are equal, don't swap
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

print(selection_sort([4, 2, 5, 3, 6, 1]))
'''


'''
def selection_sort(my_list):
    for i in range(len(my_list) -1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

print(selection_sort([1, 4, 3, 5, 6, 2]))
'''


'''
def selection_sort(my_list):
    for i in range(len(my_list) -1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

print(selection_sort([1, 4, 3, 5, 6, 2]))
'''


#'''
def selection_sort(my_list):
    for i in range(len(my_list) -1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            my_list[i], my_list[min_index] =\
            my_list[min_index], my_list[i]
    return my_list

print(selection_sort([1, 4, 3, 5, 6, 2]))
#'''