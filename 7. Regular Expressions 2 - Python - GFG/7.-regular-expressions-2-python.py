#{ 
#Driver Code Starts
#Initial Template for Python 3






import re

 # } Driver Code Ends
#User function Template for python3
import re

def validate(str):
    pat= re.compile(r'([a-z]+)([!@#$%]+)(\d+)')##your pattern here
    match = re.search(pat, str)
    if(match):
        return True
    else:
        return False



#{ 
#Driver Code Starts.

def main():
    testcases = int(input()) #testcases
    while(testcases > 0):
        str = input()
        print(validate(str))
        testcases -= 1
        


if __name__=='__main__':
    main()
#} Driver Code Ends