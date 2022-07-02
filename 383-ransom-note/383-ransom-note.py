class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l = {}
        m = {}
        for i in ransomNote:
            l[i] = 1 + l.get(i,0)
        for i in magazine:
            m[i] = 1 + m.get(i,0)
        for i in l:
            if i not in m or l[i] > m[i]:
                return False
        return True
        