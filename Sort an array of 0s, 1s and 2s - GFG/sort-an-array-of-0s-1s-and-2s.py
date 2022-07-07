#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        z = o = t = 0
        for i in arr:
            if i == 0:
                z += 1
            elif i == 1:
                o += 1
            else:
                t += 1
        for i in range(n):
            if z:
                arr[i] = 0
                z -= 1
            elif o:
                arr[i] = 1
                o -= 1
            elif t:
                arr[i] = 2
                t -= 1
        return
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