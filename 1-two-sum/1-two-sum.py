class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i, val in enumerate(nums):
            value = target - val
            if value in x:
                return [i, x[value]]
            x[val] = i
            