class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        maxp = 0
        for i,val in enumerate(prices):
            if val < minp:
                minp = val
            else:
                if maxp < val-minp:
                    maxp = val-minp
        return maxp