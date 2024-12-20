"""
List: Max Profit ( ** Interview Question)
You are given a list of integers representing stock prices for a certain company over a period of time, where each element in the list corresponds to the stock price for a specific day.

You are allowed to buy one share of the stock on one day and sell it on a later day.

Your task is to write a function called max_profit that takes the list of stock prices as input and returns the maximum profit you can make by buying and selling at the right time.

Note that you must buy the stock before selling it, and you are allowed to make only one transaction (buy once and sell once).

Constraints:



Each element of the input list is a positive integer representing the stock price for a specific day.



Function signature: def max_profit(prices):

Example:

Input: prices = [7, 1, 5, 3, 6, 4]
Function call: profit = max_profit(prices)
Output: profit = 5

Explanation: The maximum profit can be achieved by buying the stock on day 2 (price 1) and selling it on day 5 (price 6), resulting in a profit of 6 - 1 = 5.
"""
# WRITE MAX_PROFIT FUNCTION HERE #
#                                #
#                                #
#                                #
#                                #
##################################
def max_profit(prices):
    paid = 10^2
    profit = 0
    for price in prices:
        if price < paid:
            paid = price
        today = price - paid
        if today > profit:
            profit = today
        profit = max(profit, today)
    return profit

    


prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print("Test with mixed prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


prices = [7, 6, 4, 3, 1]
profit = max_profit(prices)
print("Test with descending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


prices = [1, 2, 3, 4, 5, 6]
profit = max_profit(prices)
print("Test with ascending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


"""
    EXPECTED OUTPUT:
    ----------------
    Test with mixed prices:
    Prices: [7, 1, 5, 3, 6, 4]
    Maximum profit: 5
    -----------------------------
    Test with descending prices:
    Prices: [7, 6, 4, 3, 1]
    Maximum profit: 0
    -----------------------------
    Test with ascending prices:
    Prices: [1, 2, 3, 4, 5, 6]
    Maximum profit: 5
    -----------------------------

"""

"""
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
 
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
 
    return max_profit




This code defines a function max_profit that takes a list of stock prices as input and returns the maximum profit that can be made by buying and selling the stock at the right time, with one transaction allowed.

Here's a step-by-step explanation of the code:



min_price = float('inf'):  With this line min_price is initially set to float('inf'), which represents positive infinity. This is done because the algorithm is looking for the minimum price in the list of prices. By setting min_price to infinity initially, any price in the list will be less than min_price, so min_price will be updated to that price on the first iteration of the loop.

max_profit = 0: This line initializes the max_profit variable to 0. This variable is used to store the maximum profit that can be made with a single transaction.

for price in prices:: This line starts a for loop that iterates through the list of stock prices.

min_price = min(min_price, price): This line updates the min_price variable with the minimum value between the current min_price and the current stock price in the iteration. This ensures that min_price always holds the minimum stock price seen so far.

profit = price - min_price: This line calculates the profit that could be made by buying the stock at the minimum price seen so far and selling it at the current price in the iteration.

max_profit = max(max_profit, profit): This line updates the max_profit variable with the maximum value between the current max_profit and the calculated profit. This ensures that max_profit always holds the maximum possible profit that can be made with a single transaction.

return max_profit: After the loop finishes, the max_profit variable contains the maximum profit that can be made with a single transaction. The function returns this value.



The function works by iterating through the list of prices and keeping track of the minimum price found so far. For each price in the list, it calculates the profit that could be made by buying at the minimum price and selling at the current price, and updates the maximum profit accordingly. Finally, the function returns the maximum profit.





Code with inline comments:



def max_profit(prices):
    # Initialize min_price to positive infinity
    min_price = float('inf')
    # Initialize max_profit to 0
    max_profit = 0
 
    # Iterate through the list of stock prices
    for price in prices:
        # Update min_price with the lowest price so far
        min_price = min(min_price, price)
        # Calculate profit by selling at the current price
        profit = price - min_price
        # Update max_profit with the highest profit so far
        max_profit = max(max_profit, profit)
 
    # Return the maximum profit after iterating
    return max_profit
"""