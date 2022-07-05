class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x = collections.Counter(nums)
        m = 0
        for i in x:
            if x[i] != 0:
                l,r = i-1,i+1
                c = 1
                while l in x and x[l]!= 0:
                    x[l] = 0
                    c += 1
                    l -= 1
                while r in x and x[r]!= 0:
                    x[r] = 0
                    c += 1
                    r += 1
                m = max(m, c)
        return m