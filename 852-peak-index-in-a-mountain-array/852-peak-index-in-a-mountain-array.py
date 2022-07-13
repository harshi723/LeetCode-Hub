class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r = 1, len(arr)-2
        while l<=r:
            m = (l+r)//2
            if arr[m-1] < arr[m] > arr[m+1]:
                return m
            elif arr[m-1] < arr[m] < arr[m+1]:
                l = m+1
            else:
                r = m-1
        if arr[0] > arr[1]: return arr[0]
        if arr[-1] > arr[-2]: return arr[-1]