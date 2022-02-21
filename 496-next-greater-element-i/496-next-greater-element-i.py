class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = {}
        x = []
        for i in nums2:
            while len(x) and x[-1] < i:
                l[x.pop()] = i
            x.append(i)
        for i in range(len(nums1)):
            nums1[i] = l.get(nums1[i], -1)
            
        return nums1
                