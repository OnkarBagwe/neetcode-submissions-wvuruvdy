class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        hashmap = {}
        res = 0
        for r in range(n):
            if s[r] in hashmap:
                l = max(hashmap[s[r]] + 1, l)
            hashmap[s[r]] = r
            res = max(res, r-l+1)

        return res