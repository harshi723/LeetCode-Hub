class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = []
        answer = []
        j = 1
        for i in nums:
            x.append(j)
            j *= i
        j = 1
        for i in nums[::-1]:
            x.append(j)
            j *= i
        i = 0
        j = len(x)-1
        while(j > i):
            answer.append(x[j]*x[i])
            j -= 1
            i += 1
        return answer