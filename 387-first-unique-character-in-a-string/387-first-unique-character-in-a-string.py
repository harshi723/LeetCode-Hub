class Solution:
    def firstUniqChar(self, s: str) -> int:
        x = collections.Counter(s)
        for i, val in enumerate(s):
            if x[val] == 1: return i
        return -1