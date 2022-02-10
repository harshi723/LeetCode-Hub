class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p, flag = 1, 0
        x = []
        for i in nums:
            if i != 0:
                p *= i
            else:
                flag += 1
        
        if flag > 1:
            return [0]*len(nums)
        elif flag == 1:
            for i in nums:
                if i == 0:
                    x.append(p)
                else:
                    x.append(0)
        else:
            for i in nums:
                x.append(p//i)
        
        return x