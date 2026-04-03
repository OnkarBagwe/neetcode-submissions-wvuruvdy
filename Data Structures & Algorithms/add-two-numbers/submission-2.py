# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # n1 = ""
        # n2 = ""

        # while l1:
        #     n1 = str(l1.val) + n1
        #     l1 = l1.next

        # while l2:
        #     n2 = str(l2.val) + n2
        #     l2 = l2.next

        # res = int(n1) + int(n2)

        # res = str(res)
        # res = res[::-1]

        # ans = ListNode()
        # curr = ans

        # for i in res:
        #     curr.next = ListNode(int(i))
        #     curr = curr.next

        # return ans.next

        dummy = ListNode()
        curr = dummy

        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry

            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        
        return dummy.next