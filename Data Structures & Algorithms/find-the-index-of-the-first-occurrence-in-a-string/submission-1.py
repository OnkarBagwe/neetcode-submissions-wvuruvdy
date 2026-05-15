class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # h = len(haystack)
        # n = len(needle)

        # if h == n:
        #     return 0 if haystack == needle else -1

        # for i in range(0,h-n+1):
        #     if needle in haystack[i:i+n]:
        #         return i
        # return -1

        #KMP
        if needle == "":
            return 0

        lps = [0]*len(needle)

        prevLPS = 0
        i = 1

        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]

        i = 0 # ptr for haystack
        j = 0 # ptr for needle

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]

            if j == len(needle):
                return i - len(needle)

        return -1