# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low = float("-inf"), high = float("inf")):
            if not node:
                return True
            if not(low < node.val < high):
                return False
            left_is_valid = validate(node.left, low, node.val)
            right_is_valid = validate(node.right, node.val, high)
            return left_is_valid and right_is_valid
        return validate(root)