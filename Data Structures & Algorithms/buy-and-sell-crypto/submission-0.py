from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # update minimum price so far
            if price < min_price:
                min_price = price
            # calculate profit if sold today
            profit = price - min_price
            # update max profit
            if profit > max_profit:
                max_profit = profit
        
        return max_profit
