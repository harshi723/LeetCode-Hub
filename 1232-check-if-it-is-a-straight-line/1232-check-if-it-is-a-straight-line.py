class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)==2: return True
        for i in range(2,len(coordinates)):
            a,b = coordinates[i-2][0], coordinates[i-2][1]
            x,y = coordinates[i-1][0], coordinates[i-1][1]
            m,n = coordinates[i][0], coordinates[i][1]
            area = a*(y-n) + x*(n-b) + m*(b-y)
            if area!=0: return False
        return True