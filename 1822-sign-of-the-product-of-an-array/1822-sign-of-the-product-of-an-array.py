class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 1
        for i in nums: p*= i
        if p == 0: return 0
        elif p < 0: return -1
        else: return 1