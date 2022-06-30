class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        p = 1
        f = [p]
        for i in range(1, numRows+1):
            p *= i
            f.append(p)
        
        res = []
        for i in range(numRows):
            a = []
            for j in range(i+1):
                a.append(f[i]//(f[j]*f[i-j]))
            res.append(a)
        return res