# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ""
        n2 = ""

        while l1:
            n1 = str(l1.val) + n1
            l1 = l1.next

        while l2:
            n2 = str(l2.val) + n2
            l2 = l2.next

        res = int(n1) + int(n2)

        res = str(res)
        res = res[::-1]

        ans = ListNode()
        curr = ans

        for i in res:
            curr.next = ListNode(int(i))
            curr = curr.next

        return ans.next