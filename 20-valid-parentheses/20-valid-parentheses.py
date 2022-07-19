class Solution:
    def isValid(self, s: str) -> bool:
        l = {'(':')', '[':']', '{':'}' }
        stack = []
        for i in s:
            if i in l:
                stack.append(l[i])
            else:
                if stack and stack[-1] == i:
                    stack.pop()
                else:
                    return False
        return len(stack)==0