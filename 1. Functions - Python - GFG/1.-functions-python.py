#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3
import math
##Write the function completely
def isPrime(n):
    k = int(math.sqrt(n))
    for i in range(2,k+1):
        if n%i == 0:
            return False
    return True

#{ 
#Driver Code Starts.


import math ##You will need this for prime checking

    

def main():
    testcases = int(input()) #testcases
    while(testcases > 0):
        number = int(input())
        print(isPrime(number)) ##This isPrime is function that you need to create
        testcases -= 1
        


if __name__=='__main__':
    main()
#} Driver Code Ends