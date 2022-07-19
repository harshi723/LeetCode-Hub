class Solution:
    def interpret(self, command: str) -> str:
        res = ''
        i = 0
        while i < len(command):
            if command[i] == 'G':
                res += 'G'
            elif command[i] == '(' and command[i+1] == ')':
                res += 'o'
            elif command[i] == '(':
                res += 'al'
            i += 1
        return res
            