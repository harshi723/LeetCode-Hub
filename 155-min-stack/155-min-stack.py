class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mini == None:
            self.mini = val
        elif self.mini > val:
            self.mini = val

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.mini:
            if len(self.stack) != 0:
                self.mini = min(self.stack)
            else:
                self.mini = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()