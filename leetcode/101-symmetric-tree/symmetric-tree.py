# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        q1 = []
        q2 = []

        deq_l = deque([root.left])
        deq_r = deque([root.right])

        while deq_l:
            c = deq_l.popleft()
            if c == None:
                q1.append(None)
                continue
            q1.append(c.val)
            deq_l.append(c.left)
            deq_l.append(c.right)
        
        while deq_r:
            c = deq_r.popleft()
            if c == None:
                q2.append(None)
                continue
            q2.append(c.val)
            deq_r.append(c.right)
            deq_r.append(c.left)
        return q1 == q2