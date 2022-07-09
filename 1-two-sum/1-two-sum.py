class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = {}
        for i,val in enumerate(nums):
            if target-val in l:
                return [l[target-val], i]
            l[val] = i