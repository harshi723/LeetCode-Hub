class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
#         def func(i,j,m,n):
#             if i==m-1 and j==n-1: return 1
#             elif i<0 or i==m or j<0 or j==n: return 0
#             else: return func(i,j+1,m,n) + func(i+1,j,m,n)
#         return func(0,0,m,n)
    
        # dp = [[-1 for i in range(n)] for j in range(m)]
        # def func(i,j,m,n,dp):
        #     if i==m-1 and j==n-1: return 1
        #     elif i<0 or i==m or j<0 or j==n: return 0
        #     elif dp[i][j]!=-1: return dp[i][j]
        #     else: 
        #         dp[i][j] = func(i,j+1,m,n,dp) + func(i+1,j,m,n,dp)
        #         return dp[i][j]
        # return func(0,0,m,n,dp)
        
        N = n+m-2
        r = m-1
        res = 1
        for i in range(1,r+1):
            res = res*(N-r+i)/i
        return int(res)