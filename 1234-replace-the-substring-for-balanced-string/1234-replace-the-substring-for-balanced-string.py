class Solution:
    def balancedString(self, s: str) -> int:
        x = collections.Counter(s)
        l = {}
        for i in x:
            if x[i] > len(s)//4:
                l[i] = x[i]-len(s)//4
        if not l: return 0
        
        i = 0
        res = len(s)
        for j in range(len(s)):
            if s[j] in l:
                l[s[j]] -= 1
            while max(l.values()) == 0:
                res = min(res, j-i+1)
                if s[i] in l:
                    l[s[i]] += 1
                i += 1
        return res