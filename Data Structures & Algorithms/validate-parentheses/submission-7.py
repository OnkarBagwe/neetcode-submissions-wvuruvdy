class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        closeToOpen = {')': '(', '}': '{', ']':'['}

        for c in s:
            if c in closeToOpen:
                if stk and closeToOpen[c] == stk[-1]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        
        return True if not stk else False