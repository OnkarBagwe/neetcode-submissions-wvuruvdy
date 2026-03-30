class Solution:

    def __init__(self, w: List[int]):
        self.range = -1
        self.ranges = []
        for weight in w:
            self.range += weight
            self.ranges.append(self.range)

    def pickIndex(self) -> int:
        rand_num = random.randint(0,self.range)
        l,r = 0, len(self.ranges) - 1

        while l < r:
            m = (l+r)//2
            if self.ranges[m] < rand_num:
                l = m+1
            else:
                r = m
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()