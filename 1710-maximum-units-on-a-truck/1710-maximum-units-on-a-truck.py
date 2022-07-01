class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])
        res = 0
        for i in boxTypes:
            x = min(truckSize, i[0])
            res += x*i[1]
            truckSize -= x
            if truckSize <= 0:
                break     
        return res