class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, value: int) -> None:
        self.stk.append(value)
        val = min(value, self.min_stk[-1] if self.min_stk else value)
        self.min_stk.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]
