# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def recursion(node, s):
            if not node:
                return 0
            ns = s*10 + node.val

            if node.left == None and node.right == None:
                return ns

            return recursion(node.left, ns) + recursion(node.right, ns)
        return recursion(root, 0)