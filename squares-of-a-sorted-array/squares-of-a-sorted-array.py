class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s = 0
        while s < len(nums)-1 and nums[s] < 0:
            s += 1
        n = s-1
        a = []
        for i in nums:                
            if s >= len(nums) or (n>=0 and abs(nums[n]) <= nums[s]):
                a.append(nums[n]**2)
                n -= 1
            else:
                a.append(nums[s]**2)
                s += 1
        return a