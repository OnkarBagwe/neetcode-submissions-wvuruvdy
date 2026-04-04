class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""

        countT = {}

        for c in t:
            countT[c] = 1 + countT.get(c,0)

        min_window = {}

        have = 0
        need = len(countT)

        resLen = float("inf")
        res = [-1,-1]

        l = 0

        for r in range(len(s)):
            c = s[r]
            min_window[c] = 1 + min_window.get(c,0)

            if c in countT and min_window[c] == countT[c]:
                have += 1

            while have == need:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = [l,r]
                min_window[s[l]] -= 1
                if s[l] in countT and min_window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res

        return s[l:r+1] if resLen != float("inf") else ""