#User function template for Python

class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, n, K):
		# code here
		flag = 0
		for i in range(0,n,K):
		    s,e = i,i+K-1
		    if e >= n:
		        e = n-1
		        flag = 1
		    while s <= e:
    		    arr[s], arr[e] = arr[e],arr[s]
    		    s += 1
    		    e -= 1
    		if flag == 1:
    		    return
#{ 
#  Driver Code Starts
#Initial template for Python

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()




# } Driver Code Ends