class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        x = set(s)
        y = set(t)
        if len(x)!= len(y):
            return False
        l = {}
        a = ''
        for i,j in zip(s, t):
            if i not in l:
                l[i] = j
            a += l.get(i)
        return True if a==t else False