class Solution:
    def freqAlphabets(self, s: str) -> str:
        x =[]
        i = len(s)-1
        while i>=0:
            if s[i] == '#':
                x.append(chr(int(s[i-2]+s[i-1])+96))
                i -= 3
            else:
                x.append(chr(int(s[i])+96))
                i -= 1
        res = ''
        while x:
            res += x.pop()
        return res