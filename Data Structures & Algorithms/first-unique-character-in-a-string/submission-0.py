class Solution:
    def firstUniqChar(self, s: str) -> int:
        indices = defaultdict(int)
        n = len(s)
        for i,c in enumerate(s):
            if c not in indices:
                indices[c] = i
            else:
                indices[c] = n

        res = n
        for c in indices:
            res = min(res,indices[c])

        return -1 if res == n else res