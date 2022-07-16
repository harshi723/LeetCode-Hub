class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = {}
        stack = []
        res = []
        for i in nums2:
            while stack and stack[-1]<i:
                l[stack.pop()] = i
            stack.append(i)
        for i in nums1:
            res.append(l.get(i,-1))
        return res