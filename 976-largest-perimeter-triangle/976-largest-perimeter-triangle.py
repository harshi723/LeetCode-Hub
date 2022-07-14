class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1, 1,-1):
            a,b,c = nums[i], nums[i-1], nums[i-2]
            if a+b>c and b+c>a and a+c>b:
                return a+b+c
        return 0