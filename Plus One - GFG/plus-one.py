#User function Template for python3

class Solution:
    def increment(self, arr, N):
        # code here 
        c = 1
        for i in range(N-1,-1,-1):
            x = arr[i]+c
            c = x//10
            arr[i] = x%10
            if c == 0:
                break
        if c == 1:
            res = [c] + arr
        else:
            res = arr
        return res
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ptr = ob.increment(arr,N)
        for i in ptr:
            print(i,end=" ")
        print()
# } Driver Code Ends