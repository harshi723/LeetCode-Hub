class Solution:
	def topK(self, nums, k):
        l = {}
        for i in nums:
            l[i] = l.get(i, 0) + 1
        x = [[l[i],i] for i in l]
        x.sort(reverse=True)
        res = []
        for i in range(k): res.append(x[i][1])
        return res
#{ 
#  Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	a = list(map(int, input().strip().split()))
    	n = a[0]
    	nums = a[1:]
    	k = int(input().strip())
    	obj = Solution()
    	ans = obj.topK(nums, k)
    	for i in ans:
    		print(i, end = " ")
    	print()
# } Driver Code Ends