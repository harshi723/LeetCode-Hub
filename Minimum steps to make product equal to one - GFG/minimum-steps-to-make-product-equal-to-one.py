#User function Template for python3

class Solution:
    def makeProductOne(self, arr, N):
        # code here 
        c = 0
        z = o = 0
        for i in arr:
            if i==0: 
                c += 1
                z += 1
            elif i>0: c += i-1
            else: 
                c += -1-i
                o += 1
        if o%2 != 0 and z==0:
            c += 2
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