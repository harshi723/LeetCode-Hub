class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for i in range(n):
            h = {}
            v = {}
            for j in range(n):
                he = board[i][j]
                ve = board[j][i]
                if he in h or ve in v:
                    return False
                if he!='.': h[he] = 1
                if ve!='.': v[ve] = 1
            
        for i in range(0,n,3):
            for j in range(0,n,3):
                d = {}
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l] in d:
                            return False
                        if board[k][l]!='.': d[board[k][l]] = 1
        return True