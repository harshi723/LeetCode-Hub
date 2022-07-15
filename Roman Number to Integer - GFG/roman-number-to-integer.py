#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        # code here
        l = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        c = l[S[0]]
        for i in range(1, len(S)):
            c += l[S[i]]
            if l[S[i]] > l[S[i-1]]:
                c -=  2*l[S[i-1]]
        return c
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends