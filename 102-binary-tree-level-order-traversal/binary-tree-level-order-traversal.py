# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        if root == None:
            return []
        q = deque([[root, 0]])
        while q:
            
            cv, cl = q.popleft()
            if cv == None:
                continue
            while len(ans) <= cl:
                ans.append([])

            ans[cl].append(cv.val)

            q.append([cv.left, cl+1])
            q.append([cv.right, cl+1])
        return ans