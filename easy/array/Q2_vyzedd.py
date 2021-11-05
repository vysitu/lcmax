class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        If there is no profit
        """
        if sorted(prices)[::-1] == prices:
            return 0
        
        """
        If the is profit generating
        """
        res = 0
        day = 0
        while day != len(prices) - 1:
            if prices[day] < prices[day + 1]:
                res += prices[day + 1] - prices[day]
            day += 1
        
        return res
