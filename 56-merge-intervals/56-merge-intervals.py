class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        start, end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            l,r = intervals[i][0], intervals[i][1]
            if start<=l<=end:
                end = max(end, r)
            else:
                res.append([start, end])
                start,end = l,r
        res.append([start, end])
        return res