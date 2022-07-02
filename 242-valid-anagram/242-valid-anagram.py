class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l = {}
        m = {}
        for i in s:
            l[i] = 1 + l.get(i,0)
        for i in t:
            m[i] = 1 + m.get(i,0)
        for i in m:
            if i not in l or l[i] != m[i]:
                return False
        return True