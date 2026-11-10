# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def pathSum(node):
            nonlocal res
            if not node:
                return 0

            left = pathSum(node.left)
            right = pathSum(node.right)
            left = max(left, 0)
            right = max(right, 0)

            res = max(res, node.val + left + right) #with split

            return node.val + max(left, right) #without split

        pathSum(root)
        return res