class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.maxCnt = 0
        self.stk = {}

    def push(self, val: int) -> None:
        valCnt = 1 + self.cnt.get(val,0)
        self.cnt[val] = valCnt
        if valCnt > self.maxCnt:
            self.maxCnt = valCnt
            self.stk[valCnt] = []
        self.stk[valCnt].append(val)

    def pop(self) -> int:
        res = self.stk[self.maxCnt].pop()
        self.cnt[res] -= 1
        if not self.stk[self.maxCnt]:
            self.maxCnt -= 1
        return res
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()