class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            l,r = i+1,len(numbers)-1
            while l<=r:
                m = (l+r)//2
                x = numbers[i]+numbers[m]
                if x == target:
                    return [i+1, m+1]
                elif x>target:
                    r = m-1
                else:
                    l = m+1