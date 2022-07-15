class Solution:
    def find_height(self,tree,n,k):
        # code here
        def wood(m):
            res = 0
            for i in tree:
                if i>m:
                    res += i-m
            return res
        
        l,r = 0, max(tree)
        while l<=r:
            m = (l+r)//2
            x = wood(m)
            if x == k:
                return m
            elif x<k:
                r = m-1
            else:
                l = m+1
        return -1
#{ 
#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        tree = [ int(x) for x in input().strip().split() ]
        k = int(input())
        ob=Solution()
        print(ob.find_height(tree,n,k))
# } Driver Code Ends