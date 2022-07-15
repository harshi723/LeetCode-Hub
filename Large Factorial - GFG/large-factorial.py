#User function Template for python3
class Solution:

	def factorial(self,a, n):
    	# code here
    	m = max(a)
    	res = []
    	dp = [1,1]
    	for i in range(2,m+1):
    	    dp.append((i*dp[i-1])%(10**9+7))
    	for i in a:
    	    res.append(dp[i])
        return res
#{ 
#  Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        a=list(map(int , input().strip().split()))
        ob = Solution()
        res = ob.factorial(a, n)
        for i in res:
            print(i,end=" ")
        print()
        tc=tc-1
# } Driver Code Ends