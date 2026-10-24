# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lo = 1000000001, hi = -1000000001):
            if(node != None):
                validNode = node.val < lo and node.val > hi
                return validNode and dfs(node.right, lo, max(hi, node.val)) and dfs(node.left, min(lo, node.val), hi)
            return True
            
        return dfs(root)