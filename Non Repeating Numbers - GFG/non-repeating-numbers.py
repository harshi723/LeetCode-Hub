#User function Template for python3

class Solution:
	def singleNumber(self, nums):
		# Code here
        x = 0
        for i in nums:
            x ^= i
        a = b = 0
        x = x & -x
        for i in nums:
            if i&x > 0:
                a = a^i
            else:
                b = b^i
        if a > b:
            return [b,a]
        else:
            return [a,b]
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends