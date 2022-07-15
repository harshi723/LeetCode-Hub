#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        l,m,h = 0,0,n-1
        while m<=h:
            if arr[m] == 0:
                arr[l],arr[m] = arr[m],arr[l]
                m += 1
                l += 1
            elif arr[m] == 1:
                m += 1
            else:
                arr[h],arr[m] = arr[m],arr[h]
                h -= 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends