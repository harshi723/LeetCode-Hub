class Solution:
    def firstUniqChar(self, s: str) -> int:
        x = collections.Counter(s)
        for i, val in enumerate(s):
            if x[val] == 1:
                x[val] = i
            else:
                del x[val]
        return min(x.values()) if x else -1