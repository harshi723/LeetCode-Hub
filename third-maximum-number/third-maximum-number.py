class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x = {}
        m = n = k = -sys.maxsize - 1
        for i in nums:
            if m < i:
                k = n
                n = m
                m = i
            elif n < i < m:
                k = n
                n = i
            elif k < i < n:
                k = i
        return m if k==(-sys.maxsize-1) else k