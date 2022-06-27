class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        l = 0
        for i in range(len(nums)):
            l += nums[i]
            if l-nums[i] == s-l:
                return i
        return -1
            