# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q is None and p is None:
            return True
        if q is not None and p is None:
            return False
        if q is None and p is not None:
            return False
        else:
            return (p.val == q.val) and self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)