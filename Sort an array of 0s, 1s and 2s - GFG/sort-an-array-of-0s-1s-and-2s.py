#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        # j = n-1
        # for i in range(n):
        #     while arr[j] == 2:
        #         j -= 1
        #     if arr[i] != 0:
        #         arr[i],arr[j] = arr[j],arr[i]
        #         j -= 1
        #     if i >= j:
        #         break
        arr.sort()

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