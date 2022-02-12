class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0, len(height)-1
        x = 0
        while i<j:
            m = min(height[i], height[j]) * (j-i)
            x = max(m, x)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return x