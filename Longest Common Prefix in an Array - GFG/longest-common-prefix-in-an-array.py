#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        s = arr[0]
        for i in arr:
            k = 0
            x = ''
            for j in i:
                if k<len(s) and j == s[k]:
                   x += j
                   k += 1
                else:
                    break
            s = x
        return s if s else -1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends