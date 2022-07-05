#User function Template for python3
class Solution:

	def findMaximum(self,arr, n):
		# code here
		l,r = 1, n-2
		while l<=r:
		    m = (l + r)//2
		    if arr[m] < arr[m-1]:
		        r = m-1
		    elif arr[m] < arr[m+1]:
		        l = m+1
		    else:
		        return arr[m]
		if arr[0] > arr[1]: return arr[0]
		if arr[-1] > arr[-2]: return arr[-1]
		return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends