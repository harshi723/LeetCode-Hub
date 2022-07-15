class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        s = abs(arr[0]-arr[1])
        for i in range(1, len(arr)):
            if abs(arr[i]-arr[i-1]) != s:
                return False
        return True