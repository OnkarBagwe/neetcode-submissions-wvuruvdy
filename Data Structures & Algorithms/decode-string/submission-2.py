class Solution:
    def decodeString(self, s: str) -> str:
        #one stack
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop() # remove "["
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k)*substr)

        return "".join(stack)


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