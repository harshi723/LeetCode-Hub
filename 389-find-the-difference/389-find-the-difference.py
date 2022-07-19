class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        l = {}
        for i in s:
            l[i] = l.get(i, 0) + 1
        for i in t:
            if i not in l or l[i] == 0:
                return i
            else:
                l[i] -= 1
        