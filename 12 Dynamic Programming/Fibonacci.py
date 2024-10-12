#   Requirements for DP: 1. Overlapping Subproblems | 2. Optimized Substructure

# no DP used -- Time Complexity: O(2^n) 
counter = 0
    
def fib(n):
    global counter
    counter += 1
    if n == 0 or n == 1:
        return n    # index = value in this case
    
    return fib(n - 1) + fib(n - 2)

n = 35

print('\nFib of', n, '=', fib(n))
print('Counter:', counter, "-- function calls with no DP")

###############################################################################

# Memoization Time Complexity: O(2n - 1) -> O(2n) -> O(n) by dropping constants

memo = [None] * 100  # add 0 - 99 indexes
counter = 0

def fib(n):
    global counter
    counter += 1

    if memo[n] is not None:
        return memo[n]
    
    if n == 0 or n == 1:
        return n    # index = value in this case
    
    memo[n] = fib(n - 1) + fib(n - 2)
    
    return memo[n]


n = 35

print('\nFib of', n, '=', fib(n))
print('Counter:', counter, "-- function calls with Memoization")
print(f'{counter} calls because 2 * {n} - 1 = {counter}')
print("Which is the Big O of Memoization")

###############################################################################

# Bottom Up    Time Complexity: O(n - 1) -> O(n) by dropping the non-dominant

counter = 0

def fib(n):
    fib_list = [0, 1]
    global counter

    for index in range(2, n + 1):
        counter += 1
        next_fib = fib_list[index - 1] + fib_list[index - 2]
        fib_list.append(next_fib)
    return fib_list[n]


print('\nFib of', n, '=', fib(n))
print('Counter:', counter, "-- function calls with Tabulation")
print(f'{counter} calls because {n} - 1 = {counter}')
print("Which is the Big O of Bottom Up")
