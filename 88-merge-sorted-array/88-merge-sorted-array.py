class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(m,m+n):
            nums1[i] = nums2[j]
            j += 1
        gap = (m+n+1)//2
        while gap:
            l,r = 0,gap
            while r < m+n:
                if nums1[l] > nums1[r]:
                    nums1[l], nums1[r] = nums1[r], nums1[l]
                l += 1
                r += 1
            # print(nums1, gap)
            if gap == 1: break
            gap = (gap+1)//2