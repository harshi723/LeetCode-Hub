#{ 
#Driver Code Starts
#Initial Template for Python 3


 # } Driver Code Ends
#User function Template for python3


    
power = lambda a,b: a**b##write the lambda expression in one line here


#{ 
#Driver Code Starts.    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a = int(input())
        b = int(input())
        print(power(a, b)) ##calling the anonymous function
        testcases -= 1
        


if __name__=='__main__':
    main()
#} Driver Code Ends