            # FIBONACCI number in different ways


# 1  Naive Recursion:                    Time: O(2^n) | Space: O(n)

def fib(n):
    if n < 2: return n
    return fib(n - 1) + fib(n - 2)

print(1, '->', fib(11))
###################################################################

# 2 Memoization:                           Time: O(n) | Space: O(n)

def fib2(n):
    memo = {}
    def f(x):
        if x < 2: return x
        memo[x] = f(x - 1) + f(x - 2)
        return memo[x]
    return f(n)

print(2, '->', fib2(11))
###################################################################

# 3 Tabulation:                            Time: O(n) | Space: O(n)

def fib3(n):
    if n < 2: return n
    tab = [0] * (n + 1)
    tab[0], tab[1] = 0, 1
    for i in range(2, n + 1):
        tab[i] = tab[i - 1] + tab[i - 2]
    return tab[n]

print(3, '->', fib3(11))
###################################################################

# 4 Bottom up optimized for space          Time: O(n) | Space: O(1)

def fib4(n):
    if n < 2: return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        temp = prev
        prev = curr
        curr += temp
    return curr

print(4, '->', fib4(11))
###################################################################

# 5 Binet's formula:                  Time: O(log n) | Space: O(1)

def fib5(n):
    golden_ratio = (1 + (5 ** 0.5)) / 2
    return int(round((golden_ratio ** n) / (5 ** 0.5)))

print(5, '->', fib5(11))
