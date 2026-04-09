class Solution:
    def firstUniqChar(self, s: str) -> int:
        # count = defaultdict(int)
        # n = len(s)
        # for i,c in enumerate(s):
        #     if c not in count:
        #         count[c] = i
        #     else:
        #         count[c] = n

        # res = n
        # for c in count:
        #     res = min(res,count[c])

        # return -1 if res == n else res

        #approach 2:
        count = defaultdict(int)

        for c in s:
            count[c] += 1

        for i,c in enumerate(s):
            if count[c] == 1:
                return i

        return -1