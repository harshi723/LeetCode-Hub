class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        x = -1
        while(l <= r):
            m = (l+r)//2
            if nums[m] == target:
                x = m
                break
            elif nums[m] >= nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[r] >= target > nums[m]:
                    l = m+1
                else:
                    r = m-1
        return x