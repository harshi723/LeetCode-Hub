class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False
        l = {}
        for i in s:
            l[i] = 1+l.get(i,0)
        for i in t:
            if i not in l or l[i] == 0:
                return False
            l[i] = l[i] - 1
        return True