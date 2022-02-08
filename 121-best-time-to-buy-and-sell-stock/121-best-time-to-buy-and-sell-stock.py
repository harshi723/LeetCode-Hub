class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        maxprofit = 0
        for i in range(len(prices)):
            currp = prices[i]
            if minp > currp: 
                minp = currp
            elif maxprofit < currp - minp:
                maxprofit = currp - minp
        return maxprofit