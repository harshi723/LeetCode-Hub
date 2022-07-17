class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r = 0,n
        while l<=r:
            m = (l+r)//2
            x = m*(m+1)//2
            if x == n:
                return m
            elif x > n:
                r = m-1
            else:
                l = m+1
        return r