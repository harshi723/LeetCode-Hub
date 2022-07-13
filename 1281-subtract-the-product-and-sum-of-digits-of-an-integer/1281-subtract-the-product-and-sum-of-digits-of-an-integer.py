class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s, p = 0,1
        while n:
            c = n%10
            s += c
            p *= c
            n = n//10
        return p-s