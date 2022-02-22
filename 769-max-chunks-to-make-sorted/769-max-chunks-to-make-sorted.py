class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)-1
        i = j = 0
        x = 1
        m = arr[0]
        while j < n:
            if m < arr[j]:
                m = arr[j]
            if arr[j] < arr[j+1] and j == m:
                x += 1
                i = j+1
            j += 1
        return x