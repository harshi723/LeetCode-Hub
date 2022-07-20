class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #most voting algorithm
        c = ans = 0
        for i in nums:
            if c==0:
                ans = i
            if ans == i: c+=1
            else: c -= 1
        return ans