class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = collections.Counter(nums1)
        y = collections.Counter(nums2)
        a = []
        for i in x:
            if i in y:
                a += [i]* min(x[i], y[i])
        return a