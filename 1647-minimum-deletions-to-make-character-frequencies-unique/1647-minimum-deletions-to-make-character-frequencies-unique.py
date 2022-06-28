class Solution:
    def minDeletions(self, s: str) -> int:
        freq = sorted(Counter(s).values(), reverse=True)
        x = 0
        n = len(s)
        for i in freq:
            n = min(n,i)
            x += i-n
            if n > 0:
                n -= 1
        return x