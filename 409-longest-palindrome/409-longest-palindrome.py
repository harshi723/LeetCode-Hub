class Solution:
    def longestPalindrome(self, s: str) -> int:
        l = {}
        res = maxOdd = 0
        for i in s:
            l[i] = 1 + l.get(i, 0)
        for i in l:
            if l[i] % 2 == 0:
                res += l[i]
            else:
                res += l[i] - 1
                if maxOdd < l[i]:
                    maxOdd = l[i]
        if maxOdd > 0:
            res += 1
        return res 
        