class Solution:
    def minOperations(self, logs: List[str]) -> int:
        x = []
        for i in logs:
            if i == '../' and len(x)!= 0:
                x.pop()
            elif i == './' or i == '../':
                pass
            else:
                x.append(i)
        return len(x)