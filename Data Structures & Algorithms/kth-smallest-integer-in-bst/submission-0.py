# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def findSmallest(node):
            parent = node
            while(node.left != None):
                parent = node
                node = node.left
            if(node.right != None):
                parent.left = node.right
            else:
                parent.left = None

        for i in range(k-1):
            findSmallest(root)

        while(root.left != None):
            root = root.left

        return root.val