# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        que = deque([p])
        v1 = []
        while que:
            cur = que.popleft()
            if cur == None:
                v1.append(None)
                continue
            v1.append(cur.val)
            que.append(cur.left)
            que.append(cur.right)
        
        que = deque([q])
        v2 = []
        while que:
            cur = que.popleft()
            if cur == None:
                v2.append(None)
                continue
            v2.append(cur.val)
            que.append(cur.left)
            que.append(cur.right)

        return v1 == v2