class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = collections.Counter(s)
        for i in t:
            if i not in x or x[i]==0: return False
            else:
                x[i] -= 1
        for i in x: 
            if x[i] != 0: return False
        return True