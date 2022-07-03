# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 1,n
        # res = sys.maxsize
        while l<=r:
            m = (l+r)//2
            if not isBadVersion(m):
                l = m+1
            else:
                # res = min(m,res)
                r = m-1
        return l