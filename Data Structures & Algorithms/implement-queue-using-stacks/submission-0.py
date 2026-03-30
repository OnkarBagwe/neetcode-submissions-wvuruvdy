class MyQueue:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        popped = self.q[0]
        self.q = self.q[1:]
        return popped

    def peek(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return True if len(self.q) == 0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()