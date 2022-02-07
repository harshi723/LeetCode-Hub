class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = sorted(nums)
        x = []
        l, r = 0, len(nums)-1
        while arr[l] + arr[r] != target:
            if arr[l] + arr[r] < target:
                l +=1
            elif arr[l] + arr[r] > target:
                r -= 1
            else:
                break       
        for i, val in enumerate(nums):
            if val == arr[r] or val == arr[l] and i not in x and len(x) < 2:
                x.append(i)
        return x