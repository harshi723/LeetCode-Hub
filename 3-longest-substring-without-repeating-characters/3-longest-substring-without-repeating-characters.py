class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = x = 0
        n = len(s)
        while j < n:
            if s[j] in s[i:j]:
                if j-i > x:
                    x = j-i
                i += 1
                j = i
            j += 1
        if j-i > x:
            x = j-i
        return x