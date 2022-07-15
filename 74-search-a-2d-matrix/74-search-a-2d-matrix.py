class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find(matrix,target):
            l,r = 0,len(matrix)-1
            while l<=r:
                m = (l+r)//2
                if matrix[m][0] <= target <= matrix[m][-1]:
                    return m
                elif matrix[m][0] > target:
                    r = m-1
                else:
                    l = m+1
            return -1
    
        s = find(matrix,target)
        if s == -1:
            return False
        l,r = 0,len(matrix[0])-1
        while l<=r:
            m = (l+r)//2
            if matrix[s][m] == target:
                return True
            elif matrix[s][m] > target:
                r = m-1
            else:
                l = m+1
        return False