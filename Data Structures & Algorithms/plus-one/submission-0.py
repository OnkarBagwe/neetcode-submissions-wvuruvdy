class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = ""
        for d in digits:
            n += str(d)
        n = int(n)
        n += 1
        s = str(n)
        return [int(i) for i in s]