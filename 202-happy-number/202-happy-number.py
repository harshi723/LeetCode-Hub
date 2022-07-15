class Solution:
    def isHappy(self, n: int) -> bool:
        def square(n):
            s = 0
            while n:
                s += (n%10)**2
                n = n//10
            return s
        
        l = {}
        while 1:
            res = square(n)
            if res == 1:
                return True
            if res in l:
                return False
            l[res] = 1
            n = res