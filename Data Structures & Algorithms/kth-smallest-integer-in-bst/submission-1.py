# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def inOrderDfs(node, arr):
            if node != None:
                inOrderDfs(node.left,arr)
                arr.append(node.val)
                inOrderDfs(node.right,arr)
            
        inOrderDfs(root,arr)
        return arr[k-1]