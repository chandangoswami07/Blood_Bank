def StockPicker(arr):
    varOcg = -1  # Variable to track maximum profit, initialized to -1 __define-ocg__
    
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            profit = arr[j] - arr[i]  # Calculate profit by subtracting buying price from selling price
            if profit > varOcg:
                varOcg = profit  # Update maximum profit if current profit is greater
    
    return varOcg  # Return maximum profit

# Test cases
print(StockPicker([44, 30, 24, 32, 35, 30, 40, 38, 15]))  # Output: 16
print(StockPicker([10, 9, 8, 2]))  # Output: -1
