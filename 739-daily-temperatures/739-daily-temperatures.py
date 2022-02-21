class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        x = [0]*n
        s = []
        for curr, val in enumerate(temperatures):
            while len(s) and temperatures[s[-1]] < val:
                prev = s.pop()
                x[prev] = curr - prev
            s.append(curr)
        return x