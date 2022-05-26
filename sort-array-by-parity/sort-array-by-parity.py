class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        i = j = 0
        n = len(nums)-1
        while n:
            if nums[i]%2 == 0:
                i += 1
            if nums[j]%2 != 0 or j<=i:
                j += 1
            if nums[i]%2 != 0 and nums[j]%2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
            n -= 1
        return nums