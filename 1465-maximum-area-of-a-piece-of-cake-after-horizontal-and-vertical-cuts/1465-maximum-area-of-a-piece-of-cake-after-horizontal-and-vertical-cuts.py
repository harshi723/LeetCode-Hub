class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        x = []
        y = []
        for i in range(len(horizontalCuts)):
            if i == 0:
                x.append(horizontalCuts[i])
            if i != 0:
                x.append(horizontalCuts[i]-horizontalCuts[i-1])
            if i == len(horizontalCuts)-1:
                x.append(h - horizontalCuts[i])
                
        for j in range(len(verticalCuts)):
            if j == 0:
                y.append(verticalCuts[j])
            if j == len(verticalCuts)-1:
                y.append(w - verticalCuts[j])
            if j != 0:
                y.append(verticalCuts[j]-verticalCuts[j-1])
            
        return (max(x)*max(y))%(10**9 + 7)
        
        