class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = i+1
        while j < len(nums) and i < len(nums):
            if nums[i] == 0 and nums[j] != 0:
                nums[i] = nums[j]
                nums[j] = 0
            if nums[i] != 0:
                i +=1
            if nums[j] == 0 or j <= i:
                j += 1