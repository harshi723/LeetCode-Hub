class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mini = -1
        mind = sys.maxsize
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                d = abs(x-points[i][0]) + abs(y-points[i][1])
                if mind > d:
                    mind = d
                    mini = i
        return mini