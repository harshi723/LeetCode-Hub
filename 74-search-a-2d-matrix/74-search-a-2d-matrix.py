class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[0] <= target <= i[-1]:
                s,e = 0, len(i)-1
                while s <= e:
                    m = (s+e)//2
                    if i[m] == target:
                        return True
                    elif i[m] > target:
                        e -= 1
                    else:
                        s += 1
            elif target < i[0]:
                return False
        return False