def factorial(n):
    print(f"Calculating {n}! by ")
    if n == 1:
        print("Returning the results to the previous calls")
        return 1
    return n * factorial(n - 1)

print(factorial(4))
# at one point factorial(4) will give the result as the others were calculated
# so factorial 4 = 4 * 6 (which we got from the previous runs)