def item_in_common(list1, list2):
    my_dic = {}

    for i in list1:
        my_dic[i] = True
    
    for j in list2:
        if j in my_dic:
            return True

    return False


list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))
# since 5 is in both lists, it should return True

"""
SOLUTION using a SET:

    my_set = set(list1)    

    for i in list2:
        if i in my_set:
            return True
    return False

"""