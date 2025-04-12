def maxProfit(prices):
    # Initialize variables
    min_price = float('inf')  # Set min_price to infinity initially
    max_profit = 0  # Set initial max_profit to 0
    
    # Traverse through the prices array
    for price in prices:
        # Update the min_price if the current price is lower
        min_price = min(min_price, price)
        
        # Calculate the potential profit if we sell at the current price
        profit = price - min_price
        
        # Update the max_profit if the current profit is higher
        max_profit = max(max_profit, profit)
    
    return max_profit

# Input
prices = [int(input()) for _ in range(int(input()))]  # Taking prices input one by one

# Output
print(maxProfit(prices))  # Prints the maximum profit
