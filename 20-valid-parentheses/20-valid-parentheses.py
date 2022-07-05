class Solution:
    def isValid(self, s: str) -> bool:
        l = {
            '(':')', '[':']', '{':'}'
        }
        arr = []
        for i in s:
            if i in l:
                arr.append(l[i])
            else:
                if not arr or i!=arr.pop():
                    return False
        return len(arr)==0