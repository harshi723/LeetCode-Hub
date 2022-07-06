class Solution:
    def __init__(self):
        self.l = {}
        
    def climbStairs(self, n: int) -> int:
        if n in self.l:
            return self.l[n]
        elif n < 3:
            return n
        else:
            x = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.l[n] = x
            return x