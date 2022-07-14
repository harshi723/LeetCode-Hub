class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        ans = [[1],[1,1]]
        for i in range(2,numRows):
            x = [1]
            for k in range(1,i):
                x.append(ans[-1][k-1]+ans[-1][k])
            x.append(1)
            ans.append(x)
        return ans