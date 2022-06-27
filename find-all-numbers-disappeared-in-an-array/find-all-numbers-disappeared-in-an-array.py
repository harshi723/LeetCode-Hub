class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            x = abs(i)-1
            if nums[x] > 0:
                nums[x]*=-1
        a = []
        for i in range(len(nums)):
            if nums[i] > 0:
                a.append(i+1)
        return a