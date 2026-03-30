class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = [] # [char,cnt]

        for c in s:
            if stk and stk[-1][0] == c:
                stk[-1][1] += 1
            else:
                stk.append([c,1])
            if stk[-1][1] == k:
                stk.pop()

        res = ""

        for char,cnt in stk:
            res += (char*cnt)
        
        return res