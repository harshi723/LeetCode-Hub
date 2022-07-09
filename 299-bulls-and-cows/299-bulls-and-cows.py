class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        l = {}
        b = c = 0
        for i in secret:
            l[i] = 1 + l.get(i,0)
        for i in guess:
            if i in l and l[i] > 0:
                c += 1
                l[i] -= 1
        for i,j in zip(secret, guess):
            if i == j: b += 1
        return str(b)+'A'+str(c-b)+'B'