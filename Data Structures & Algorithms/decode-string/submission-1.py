class Solution:
    def decodeString(self, s: str) -> str:
        #one stack
        stk = []

        for i in range(len(s)):
            if s[i] != "]":
                stk.append(s[i])
            else:
                substr = ""
                while stk[-1] != "[":
                    substr = stk.pop() + substr
                stk.pop()
                k = ""
                while stk and stk[-1].isdigit():
                    k = stk.pop() + k
                
                stk.append(int(k)*substr)
        
        return "".join(stk)


        #two stack
        # string_stack = []
        # count_stack = []
        # cur = ""
        # k = 0

        # for c in s:
        #     if c.isdigit():
        #         k = k * 10 + int(c)
        #     elif c == "[":
        #         string_stack.append(cur)
        #         count_stack.append(k)
        #         cur = ""
        #         k = 0
        #     elif c == "]":
        #         temp = cur
        #         cur = string_stack.pop()
        #         count = count_stack.pop()
        #         cur += temp * count
        #     else:
        #         cur += c

        # return cur