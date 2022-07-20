class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i<len(nums):
            j = i+1
            while j<len(nums):
                x = target - nums[i] - nums[j]
                l,r = j+1,len(nums)-1
                while l<r:
                    if nums[l]+nums[r] > x: r-=1
                    elif nums[l]+nums[r] < x: l+=1
                    else:
                        temp = []
                        temp.append(nums[i])
                        temp.append(nums[j])
                        temp.append(nums[l])
                        temp.append(nums[r])
                        res.append(temp)
                        while l<r and nums[l]==temp[2]: l+=1
                        while l < r and nums[r]==temp[3]: r-=1
                while j+1<len(nums) and nums[j+1]==nums[j]: j+=1
                j+=1
            while i+1<len(nums) and nums[i+1]==nums[i]: i+=1
            i += 1
        return res
                    