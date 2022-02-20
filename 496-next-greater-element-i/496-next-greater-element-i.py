class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = {}
        x = []
        y = []
        for i in reversed(nums2):
            if len(x) == 0:
                x.append(i)
                l[i] = -1
            elif i >= x[-1]:
                while len(x) > 0:
                    if i < x[-1]:
                        l[i] = x[-1]
                        x.append(i)
                        break
                    x.pop()
                if i not in l:
                    l[i] = -1
                    x.append(i)
            else:
                l[i] = x[-1]                
                x.append(i)
        for i in nums1:
            y.append(l[i])
        return y