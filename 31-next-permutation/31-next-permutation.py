class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, l, r):
            while l<=r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
                
        if len(nums)==1: return 
        x = len(nums)-2
        while x>=0 and nums[x] >= nums[x+1]: x -= 1
        if x>=0:
            j = len(nums)-1
            while nums[x] >= nums[j]: j-= 1
            nums[x], nums[j] = nums[j], nums[x]
            # print(x,j,nums)
        reverse(nums, x+1, len(nums)-1)
        