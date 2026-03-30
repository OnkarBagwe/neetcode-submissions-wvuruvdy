class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
        # hashmap = {}
        # res = 0
        # temp = 0
        # sub = ""
        # for c in s:
        #     print("c: ", c)
        #     if c not in hashmap:
        #         temp += 1
        #         sub += c
        #         print(sub)
        #         print("temp: ", temp)
        #         hashmap[c] = 1
        #     elif c in hashmap:
        #         res = max(res, temp)
        #         print("res: ", temp)
        #         hashmap[c] = 1
        #         temp = len(sub)
        #         sub = sub[s.index(c)+1::]
        # return max(res, temp)