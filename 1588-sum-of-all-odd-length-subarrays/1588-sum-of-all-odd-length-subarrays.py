class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        i = s = 0
        while i < len(arr)-1:
            j = i+1
            while j <= len(arr):
                s += sum(arr[i:j])
                j += 2
            i += 1
        s += arr[-1]
        return s