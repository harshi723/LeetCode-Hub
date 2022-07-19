class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for i in grid:
            l,r = 0, len(i)-1
            while l<=r:
                m = (l+r)//2
                if i[m] >= 0:
                    l = m+1
                else:
                    r = m-1
            res += len(i)-l
        return res