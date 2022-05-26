class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr = [nums[0]]
        j = 0
        for i in range(len(nums)):
            if i != 0 and nums[i] != arr[j]:
                arr.append(nums[i])
                j += 1
        for i in range(len(nums)):
            if i < len(arr):
                nums[i] = arr[i]
            else:
                nums.pop()
            