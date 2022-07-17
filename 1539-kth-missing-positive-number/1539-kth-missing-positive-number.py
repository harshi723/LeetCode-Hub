class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        for j in arr:
            while j != i:
                k -= 1
                if k == 0:
                    return i
                i += 1
            if j == i:
                i += 1
        while k:
            k -= 1
            i += 1
        return i-1