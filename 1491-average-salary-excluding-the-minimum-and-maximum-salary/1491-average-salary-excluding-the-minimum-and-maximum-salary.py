class Solution:
    def average(self, salary: List[int]) -> float:
        m,n,s = min(salary), max(salary), sum(salary)
        s = s - m - n
        avg = s/(len(salary)-2)
        return avg