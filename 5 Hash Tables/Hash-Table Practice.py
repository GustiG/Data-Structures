'''class HashTable:    # initializes a list from 0-6
    def __init__(self, size = 7): # list should have a prime number
        self.data_map = [None] * size # for increased randomness


    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % \
            len(self.data_map)
        return my_hash'''

"""
First we create the size of the list. 0-6 in this case
and initialize all these addresses to None

Second:
define the hash method by using the ASCII number for each letter 
in key and multiply it by a prime number (here 23) and getting the 
reminder (modulo %) of the data_map's length (0-6) -- divide any
number by 7 and you'll get a remainder of 0 to 6, thus giving 
the address where the key-value pair will go
"""
'''
modulo gives back the remainder of the division as a result.
7%3 = how much of 7 will be left over after 7 is divided by 3
7 items are put into 3 groups with a result of 2 groups and 1
item left
7//3=2 | 2*3=6 | 7-6=1
'''
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
                (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash      

'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)


my_hash_table = HashTable()
my_hash_table.print_table()
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_value(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])


my_hash_table = HashTable()
my_hash_table.set_value('bolts', 1000)
my_hash_table.set_value('washers', 50)
my_hash_table.set_value('lumber', 70)
my_hash_table.print_table()
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    # OR
    # def print_table(self):
    #     index = 0
    #     for val in self.data_map:
    #         print(index, ": ", val)
    #         index += 1

    def set_value(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])


my_hash_table = HashTable()
my_hash_table.set_value('bolts', 1000)
my_hash_table.set_value('washers', 50)
my_hash_table.set_value('lumber', 70)
my_hash_table.print_table()
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        index = 0
        for val in self.data_map:
            print(index, ": ", val)
            index += 1

    def set_value(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

ht = HashTable()
ht.set_value('Gusti', 37)
ht.set_value('Andreea', 43)
ht.set_value('Victor', 6)
ht.print_table()
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % (len(self.data_map))
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])


ht = HashTable()
ht.set_item('Gusti', 37)
ht.set_item('Andreea', 43)
ht.set_item('Victor', 6)
ht.print_table()
print("ai parcurs", round(116/238*100, 2), "% din curs\
      \nFelicitari!")
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % (len(self.data_map))
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])


ht = HashTable()
ht.set_item('Gusti', 37)
ht.set_item('Andreea', 43)
ht.set_item('Victor', 6)
ht.print_table()
print("ai parcurs", round(116/238*100, 2), "% din curs\
      \nFelicitari!")
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % (len(self.data_map))
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

ht = HashTable()
ht.set_item('cuie', 40)
ht.set_item('ciocane', 4)
ht.set_item('modafinil', 0.5)
ht.print_table()
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []    
        self.data_map[index].append([key, value])

ht = HashTable()
ht.set_item('Gusti', 37)
ht.set_item('Andreea', 43)
ht.set_item('Victor', 6)
ht.print_table()
print("ai parcurs", round(116/238*100, 2), "% din curs\
      \nFelicitari!")
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        index = 0
        for val in self.data_map:
            print(index, ": ", val)
            index += 1
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])


ht = HashTable()
ht.set_item('Gusti', 37)
ht.set_item('Andreea', 43)
ht.set_item('Victor', 6)
ht.print_table()
print("ai parcurs", round(116/238*100, 2), "% din curs\
      \nFelicitari!")
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])


ht = HashTable()
ht.set_item('Fifi', 5)
ht.set_item('Gigi', 10)
ht.set_item('Didi', 6)
ht.print_table()
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

ht = HashTable()
ht.set_item('Gigi', 33)
ht.set_item('Didi', 44)
ht.set_item('Fifi', 00)
ht.set_item('Coco', 5.99)
ht.set_item('Lala', 21)
ht.set_item('Sisi', 0.9)
ht.set_item('Mimi', 88)
ht.set_item('Nono', 9000)
ht.print_table()
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []        
        self.data_map[index].append([key, value])

my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1000)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()
print("ai parcurs", round(116/238*100, 2), "% din curs\
      \nFelicitari!")
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * 7

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val) 
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

ht = HashTable()
ht.set_item('Bobi', 4900)
ht.set_item('Spencer', 657)
ht.set_item('Kilminster', 777)
ht.print_table()
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * 7

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None


my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1000)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('Washers'))
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    

ht = HashTable()
ht.set_item('Gusti', 33)
ht.set_item('Andreea', 12)
ht.set_item('Victor', 99)
ht.print_table()
print(ht.get_item('Gusti'))
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print (i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
ht = HashTable()
ht.set_item('Anglia', 2)
ht.set_item('Spania', 1)
ht.set_item('Romania', 14)
ht.print_table()
print(ht.get_item('Anglia'))
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1000)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('Washers'))
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])


    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] != None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    

my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1000)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('Washers'))
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if not self.data_map[index]:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []    
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    
    
my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1000)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('Washers'))
print(my_hash_table.keys())
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1000)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('Washers'))
print(my_hash_table.keys())
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map) 
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    


my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1000)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('Washers'))
print(my_hash_table.keys())
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:
            for i in range(len(self.data_map)):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    


my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1000)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('Washers'))
print(my_hash_table.keys())
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val, in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


ht = HashTable()
ht.set_item('Wasyle', 88)
ht.set_item('Vegeta', 9000)
ht.print_table()
print(ht.get_item('Vegeta'))
print(ht.keys())
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    

my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1000)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('Washers'))
print(my_hash_table.keys())
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    
my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1000)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('Washers'))
print(my_hash_table.keys())
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    

my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1000)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('Washers'))
print(my_hash_table.keys())
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    
my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1000)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('Washers'))
print(my_hash_table.keys())
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % (len(self.data_map))
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    

    
my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1000)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('Washers'))
print(my_hash_table.keys())
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    
my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1000)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('Washers'))
print(my_hash_table.keys())
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    

my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1000)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('Washers'))
print(my_hash_table.keys())
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):       # pick a prime number
        self.data_map = [None] * size   # a list on 7 with Nones
    
    def __hash(self, key):              # defining the hash
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    

my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1000)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('Washers'))
print(my_hash_table.keys())
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []   # create a list if empty
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

ht = HashTable()
ht.set_item('Gigi', 2000)
ht.set_item('Fifi', 2024)
ht.set_item('Mimi', 1111)
ht.print_table()
print(ht.get_item('Gigi'))
print(ht.keys())
'''
################################################################
################################################################
################################################################
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = \
            (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        for i in range(len(self.data_map[index])):
            if self.data_map[index][i][0] == key:
                return self.data_map[index][i][1]
        return None
            
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    

ht = HashTable()
ht.set_item('Gigi', 2000)
ht.set_item('Fifi', 2024)
ht.set_item('Mimi', 1111)
ht.print_table()
print(ht.get_item('Gigi'))
print(ht.keys())
'''
################################################################
################################################################
################################################################

# class HashTable:
#     def __init__(self, size=7):
#         self.data_map = [None] * size
    
#     def __hash(self, key):
#         my_hash = 0
#         for letter in key:
#             my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
#         return my_hash

#     def print_table(self):
#         for i, val in enumerate(self.data_map):
#             print(i, ": ", val)
    
#     def set_item(self, key, value):
#         index = self.__hash(key)
#         if self.data_map[index] is None:
#             self.data_map[index] = []
#         self.data_map[index].append([key, value])

#     def get_item(self, key):
#         index = self.__hash(key)
#         # Check if the bucket is None
#         if self.data_map[index] is None:
#             return None
#         for pair in self.data_map[index]:
#             if pair[0] == key:
#                 return pair[1]
#         return None

    
#     def keys(self):
#         all_keys = []
#         for i in range(len(self.data_map)):
#             if self.data_map[i] is not None:
#                 for j in range(len(self.data_map[i])):
#                     all_keys.append(self.data_map[i][j][0])
#         return all_keys

    

# my_hash_table = HashTable()
# my_hash_table.set_item('bolts', 1000)
# my_hash_table.set_item('washers', 50)
# my_hash_table.set_item('lumber', 70)
# my_hash_table.print_table()
# print(my_hash_table.get_item('washers'))
# print(my_hash_table.get_item('Washers'))
# print(my_hash_table.keys())

################################################################
################################################################
################################################################

