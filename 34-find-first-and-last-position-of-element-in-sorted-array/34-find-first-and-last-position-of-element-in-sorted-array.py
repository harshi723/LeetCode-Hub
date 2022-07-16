class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0,len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]<target:
                l = m+1
            else:
                r = m-1
        if l<0 or l==len(nums) or nums[l]!=target: return [-1,-1]
        first = l
        l,r = 0,len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]>target:
                r = m-1
            else:
                l = m+1
        last = r
        return [first, last]