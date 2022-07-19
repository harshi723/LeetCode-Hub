class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = sys.maxsize
        maxprofit = 0
        for i in prices:
            minprice = min(minprice, i)
            maxprofit = max(maxprofit, i-minprice)
        return maxprofit