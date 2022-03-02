class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = {}
        for i in strs:
            x = ''.join(sorted(i))
            l[x] = [i] + l.get(x, [])
        return l.values()