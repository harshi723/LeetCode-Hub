class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans, m = 1, n
        if m<0: m*= -1
        while m:
            if m%2==0:
                x = x*x
                m = m//2
            else:
                ans = ans*x
                m = m-1
        return ans if n>0 else 1/ans