#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        # code here
        x = []
        y = []
        for i in arr:
            if i>=0:
                x.append(i)
            else: 
                y.append(i)
        a,b = 0,0
        for i in range(n):
            if i%2==0:
                if a<len(x):
                    arr[i] = x[a]
                    a += 1
                else:
                    arr[i] = y[b]
                    b += 1
            else:
                if b<len(y):
                    arr[i] = y[b]
                    b += 1
                else:
                    arr[i] = x[a]
                    a += 1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends