class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0,len(matrix)-1
        i = 0
        flag = False
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                i = mid
                flag = True
                break
            elif matrix[mid][0] > target:
                r -= 1
            else:
                l += 1
        if not flag: return False
                
        
        s,e = 0, len(matrix[i])-1
        while s <= e:
            m = (s+e)//2
            if matrix[i][m] == target:
                return True
            elif matrix[i][m] > target:
                e -= 1
            else:
                s += 1
        return False