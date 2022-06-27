class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        m = nums[0]
        for i in nums:
            s += i
            m = max(s, m)
            if s < 0: s = 0
        return m