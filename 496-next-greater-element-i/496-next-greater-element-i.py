class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = {}
        x = []
        y = []
        for i in reversed(nums2):
            while len(x) > 0 and i >= x[-1]:
                if i < x[-1]:
                    break
                x.pop()
            if len(x) == 0:
                l[i] = -1                
                x.append(i)
            if i < x[-1]:
                l[i] = x[-1]                
                x.append(i)
        for i in nums1:
            y.append(l[i])
        return y