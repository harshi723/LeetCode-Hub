class Solution:
    def countOdds(self, low: int, high: int) -> int:
        c1 = low//2
        c2 = high //2
        # if low%2 == 1: c1+=1
        if high%2 == 1: c2+=1
        return c2-c1