class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        x = []
        nums.sort()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    if [nums[i], nums[j], nums[k]] not in x:
                        x.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
        return x