class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        m = nums[0]
        for i in nums:
            if s+i >= i:
                s += i
            else:
                s = i
            m = max(m, s)
        return m