class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l = {}
        for i in t:
            l[i] = 1 + l.get(i,0)
        for i in s:
            if i not in l or l[i] == 0:
                return False
            l[i] -= 1
        return True