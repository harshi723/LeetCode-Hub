class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count = smaller = 0
        x = []
        for i in nums:
            if i == target:
                count += 1
            elif i < target:
                smaller += 1
        for i in range(count):
            x.append(smaller)
            smaller += 1
        return x