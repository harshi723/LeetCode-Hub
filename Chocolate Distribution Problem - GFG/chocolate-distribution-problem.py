#User function Template for python3
import sys
class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        A.sort()
        # print(A)
        m = sys.maxsize
        for i in range(N-M+1):
            s = A[M-1+i] - A[i]
            if m > s:
                m = s
        return m
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends