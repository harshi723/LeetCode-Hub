class Solution:
    def makeGood(self, s: str) -> str:
        x = []
        for i in s:
            if len(x) != 0:
                if (ord(i)-97 == ord(x[-1])-65) or (ord(i)-65 == ord(x[-1])-97):
                    x.pop()
                else:
                    x.append(i)
            else:
                x.append(i)
        return ''.join(x)