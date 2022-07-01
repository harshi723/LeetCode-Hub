class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            h = {}
            v = {} 
            for j in range(9):
                currh = board[i][j]
                currv = board[j][i]
                if (currh!='.' and currh in h) or (currv!='.' and currv in v):
                    return False
                h[currh] = 1
                v[currv] = 1
        
        e = f = 0
        for i in range(9):
            l = {}
            for j in range(3):
                for k in range(3):
                    x = board[j+e][k+f]
                    if x!='.' and x in l:
                        return False
                    l[x] = 1
            e += 3
            if e == 9:
                e = 0
                f += 3
        return True