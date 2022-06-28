class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s))!= len(set(t)):
            return False
        l = {}
        for i,j in zip(s, t):
            if i not in l:
                l[i] = j
            if l.get(i) != j:
                return False
        return True