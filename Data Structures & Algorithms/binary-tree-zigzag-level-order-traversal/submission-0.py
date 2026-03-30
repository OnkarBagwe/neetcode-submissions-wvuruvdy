# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stk = [(root,0)]
        res = []
        while stk:
            node,depth = stk.pop()
            if depth == len(res):
                res.append([])
            
            res[depth].append(node.val)

            if node.right:
                stk.append((node.right,depth+1))
            if node.left:
                stk.append((node.left,depth+1))
        
        for i in range(len(res)):
            if i%2:
                res[i].reverse()
        return res
