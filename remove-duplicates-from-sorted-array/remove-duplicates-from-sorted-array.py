class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = i + 1
        n = len(nums)
        while j < n:
            if nums[i] == nums[j]:
                nums.pop(j)
                n -= 1
            else:
                i += 1
                j += 1
            