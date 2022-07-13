class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        maxprofit = 0
        for i in range(len(prices)):
            if minp > prices[i]:
                minp = prices[i]
            elif maxprofit < prices[i] - minp:
                maxprofit = prices[i]-minp
        return maxprofit