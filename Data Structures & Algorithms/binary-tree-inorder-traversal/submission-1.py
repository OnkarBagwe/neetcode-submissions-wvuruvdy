# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #recursive

        def inorder(node):
            if not node:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(node.right)

        inorder(root)
        return res
        
        #iterative
        # stk = []
        # res = []
        # curr = root

        # while curr or stk:
        #     while curr:
        #         stk.append(curr)
        #         curr = curr.left
        #     curr = stk.pop()
        #     res.append(curr.val)
        #     curr = curr.right

        # return res