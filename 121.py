def maxProfit(self, prices):
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)

    return max_profit

'''
Solution 1.

def maxProfit(self, prices):
    # brute-force
    
    max_profit = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)

    return max_profit


Solution 2.
# Kadane Algorithm
# Time: O(n)
# Space: O(1)

def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_current = 0
    max_far = 0

    for i in range(1, len(prices)):
        diff = prices[i] - prices[i - 1]
        max_current = max(0, max_current + diff)  # if negative number, restart
        max_far = max(max_far, max_current)

    return max_far
    
'''
