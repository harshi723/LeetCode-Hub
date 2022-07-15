#User function Template for python3

class Solution:
    def indexes(self, v, x):
        # Your code goes here
        def search(v,x):
            l,r = 0,len(v)-1
            while l<=r:
                m = (l+r)//2
                if v[m] == x:
                    return m
                elif v[m] > x:
                    r = m-1
                else:
                    l = m+1
            return -1
        
        res = search(v,x)
        if res == -1: 
            return [-1,-1]
        else:
            l = r = res
            while l>=0 and v[l] == x:
                l -= 1
            while r<len(v) and v[r]==x:
                r += 1
        return [l+1,r-1]
#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        obj = Solution()
        ans = obj.indexes(a, k)
        if ans[0]==-1 and ans[1]==-1:
            print(-1)
        else:
            print(ans[0], end=' ')
            print(ans[1])

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends