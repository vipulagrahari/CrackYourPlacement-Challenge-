# 121. Best Time to Buy and Sell Stock
# Easy

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

#approach: we keep two pointers and update the hightest profit when we find a combination of min and max components


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mn, mx = float('inf'), 0

        for i in range(len(prices)):
            
            mn= min(prices[i],mn)
            mx= max(mx, prices[i]-mn)
        
        return mx