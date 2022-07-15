#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        p = 1
        z = 0
        for i in nums:
            if i== 0: 
                z += 1
            else:
                p *= i
            
        res = []
        for i in nums:
            if z==0:
                res.append(p//i)
            elif z > 1:
                res.append(0)
            else:
                if i==0:
                    res.append(p)
                else:
                    res.append(0)
        return res
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends