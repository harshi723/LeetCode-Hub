class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3 or arr[0] > arr[1]:
            return False
        i = m = 0
        j = i+1
        while j<len(arr):
            if arr[i] > arr[j]:
                m = i
                break
            if arr[i] == arr[j]:
                return False
            i += 1
            j += 1
        if m == 0 or m == len(arr):
            return False
        j = m+1
        while j<len(arr):
            if arr[m] > arr[j]:
                m += 1
                j += 1
            else:
                return False
        return True