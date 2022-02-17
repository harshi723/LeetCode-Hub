class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = []
        for i in nums1:
            flag = 0
            for j in nums2[nums2.index(i):]:
                if j > i:
                    x.append(j)
                    flag = 1
                    break
            if flag == 0:
                x.append(-1)
        return x