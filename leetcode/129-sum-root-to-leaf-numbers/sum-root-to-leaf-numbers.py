# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def recursive(node, v):
            nonlocal ans
            nv = v*10+node.val
            if not node.left and not node.right:
                ans += nv

            if node.left:
                print("left")
                recursive(node.left, nv)
            if node.right:
                print('right')
                recursive(node.right, nv)

        recursive(root, 0)
        return ans