class Solution:
    def longestPalindrome(self, s: str) -> int:
        x = collections.Counter(s)
        c = 0
        flag = 0
        for i in x:
            if x[i]%2 == 0:
                c += x[i]
            else:
                c += x[i]-1
                flag = 1
        if flag == 1:
            c += 1
        return c