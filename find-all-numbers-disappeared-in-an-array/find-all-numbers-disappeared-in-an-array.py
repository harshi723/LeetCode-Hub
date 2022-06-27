class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x = len(nums)
        l = {}
        a = []
        for i in nums:
            l[i] = l.get(i, 1)
        for i in range(1, x+1):
            if i not in l:
                a.append(i)
        return a