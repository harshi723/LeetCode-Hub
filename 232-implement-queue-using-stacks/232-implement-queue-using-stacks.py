class MyQueue:

    def __init__(self):
        self.q = []
        self.r = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        if not self.r:
            while self.q:
                self.r.append(self.q.pop())
        return self.r.pop()

    def peek(self) -> int:
        return self.q[0] if not self.r else self.r[-1]
    
    def empty(self) -> bool:
        return len(self.q) == len(self.r) ==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()