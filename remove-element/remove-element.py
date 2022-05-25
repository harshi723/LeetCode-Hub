class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums.pop(i)
                i = 0
                n -= 1
            else:
                i += 1