class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = 0
        for i in range(len(arr)-1):
            if i == m:
                j = m = i+1
                while j < len(arr):
                    if arr[j] > arr[m]:
                        m = j
                    j += 1
            arr[i] = arr[m]
        arr[-1] = -1
        return arr