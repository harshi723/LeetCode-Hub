class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        l = {}
        for i in range(len(arr)):
            if (arr[i]*2 in l) or (arr[i]%2 == 0 and arr[i]//2 in l):
                return True
            l[arr[i]] = i*2
            print(l[arr[i]])
        return False
                
            