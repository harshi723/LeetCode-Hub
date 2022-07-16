class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        x = collections.Counter(magazine)
        for i in ransomNote:
            if i not in x or x[i]==0: return False
            else:
                x[i] -= 1
        return True