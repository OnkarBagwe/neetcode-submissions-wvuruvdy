class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # charSet = set()
        # l = 0
        # res = 0
        # for r in range(len(s)):
        #     while s[r] in charSet:
        #         charSet.remove(s[l])
        #         l += 1
        #     charSet.add(s[r])
        #     res = max(res, r - l + 1)
        # return res
        hashmap = {}
        res = 0
        l = 0

        for r in range(len(s)):
            if s[r] in hashmap:
                l = max(hashmap[s[r]] + 1, l)
            hashmap[s[r]] = r
            res = max(res, r - l + 1)
        return res