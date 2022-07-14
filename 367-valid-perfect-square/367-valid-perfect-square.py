class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = 1
        while num>0:
            num -= x
            x += 2
        return num==0