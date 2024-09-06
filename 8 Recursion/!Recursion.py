        # Time complexity: O(<times its called> ^ n)

# def sum_n(n):
#     if n == 0:
#         return 0
#     return n + sum_n(n - 1)

# print(sum_n(100))

##############################################################

# def sum_digits(n):
#     if n == 0:
#         return 0
    
#     last_digit = n % 10
#     remaining = n // 10
#     # print(remaining, last_digit)

#     return sum_digits(remaining) + last_digit

# print(sum_digits(1113312))

##############################################################

# def pattern_print(n):
#     if n == 0:
#         return
    
#     for i in range(n):
#         print(i + 1, end=" ") # i + 1 to avoid printing zeroes
#     print()

#     pattern_print(n - 1)   # move this above the loop 
#                             # to flip the pattern
    
# pattern_print(8)

##############################################################
'''
def print_pattern(n):
    if n == 0:
        return
    
    print_pattern(n - 1)    # only after all the calls are executed, the
                            # result is returned
    print(n)                # hence n appears as 1 first
    for i in range(n):
        print(i + 1, end=" ")
    print()


print_pattern(8)
'''

##############################################################
'''
def print_pattern(n):
    if n == 1:
        print(1)
        return
    
    for i in range(n):
        print(i + 1, end=" ")
    print()

    print_pattern(n - 1)

    for i in range(n):
        print(i + 1, end=" ")
    print()


print_pattern(4)
'''

##############################################################
'''
def addDigits(n):
    if n == 0:
        return 0
    
    lastDigit = n % 10
    remaining = n // 10

    return addDigits(remaining) + lastDigit


print(addDigits(1314))
'''

##############################################################
'''
def pp(n):
    if n == 1:
        print(1)
        return
    
    for i in range(n):
        print(i + 1, end=" ")
    print()

    pp(n - 1)

    for i in range(n):
        print(i + 1, end=" ")
    print()

pp(4)
'''

##############################################################
'''
def factorial(n):
    if n == 1:
        return 1 
    
    return n * factorial(n - 1)

print(factorial(4))
'''

##############################################################
'''
def sayHello(n):
    if n == 0:
        return 0
    
    sayHello(n - 1)     
    print("Hello", n)


sayHello(4)
'''

##############################################################
'''
def numSum(n):
    if n == 0: return 0
    print(f'n is now {n}')
    return n + numSum(n - 1)
    
print(numSum(4))
'''

##############################################################
'''
def pp(n):
    if n == 0: return

    pp(n - 1)
    for i in range(n):
        print(i + 1, end=" ")
    print()


pp(4)
'''

##############################################################
'''
def pp(n):
    if n == 0: return

    for i in range(n):
        print(i + 1, end=" ")
    print()

    pp(n - 1)


pp(4)
'''

##############################################################
'''
def pp(n):
    if n == 1:
        print(1)
        return

    for i in range(n):
        print(i + 1, end=" ")
    print()

    pp(n - 1)

    for i in range(n):
        print(i + 1, end=" ")
    print()


pp(4)
'''

##############################################################
'''
def sayHello(n):
    if n == 0:
        return
    
    sayHello(n - 1)         # move this line under print to 
    print("Hello", n)       # count backwards
    

sayHello(4)
'''

##############################################################
'''
def addDigits(n):
    if n == 0:
        return 0
    
    last_digit = n % 10
    remaining = n // 10

    print(remaining, "|", last_digit)
    return addDigits(remaining) + last_digit


print(addDigits(13141))
'''

##############################################################
'''
def factorial(n):
    if n == 1: return 1

    return n * factorial(n - 1)


print(factorial(4))
'''

##############################################################
'''
def numSum(n):
    if n == 0: return 0

    return n + numSum(n - 1)


print(numSum(10))
'''

# made the above function without recursion because it's great:
'''
def numSum(n):
    half = n // 2
    firstPlusLast = 1 + n
    result = half * firstPlusLast
    return result

print(numSum(10))
'''

##############################################################
