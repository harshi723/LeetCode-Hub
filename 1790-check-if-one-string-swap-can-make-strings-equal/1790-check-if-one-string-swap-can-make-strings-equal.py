class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c = 0
        l = {}
        for i in s1:
            l[i] = l.get(i,0) + 1
        for i in s2:
            if i not in l or l[i] == 0:
                return False
            else:
                l[i] -= 1
        for i,j in zip(s1,s2):
            if i!=j: c+= 1
        return c<3