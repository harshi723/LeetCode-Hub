#User function Template for python3

class Solution:
    def makeProductOne(self, arr, N):
        # code here 
        c = zc = nc = 0
        for i in arr:
            if i > 0:
                c += (i-1)
            elif i < 0:
                c += abs(i)-1
                nc += 1
            else:
                zc += 1
        if nc%2!=0 and zc==0:
            c += 2
        c += zc
        return c

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.makeProductOne(arr,N))
# } Driver Code Ends