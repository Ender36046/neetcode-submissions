# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        highest = root.val
        numGood = 0
        
        def dfs(root, highestVal):
            if(not root is None):
                nonlocal numGood
                if(highestVal <= root.val):
                    numGood +=1
                dfs(root.left, max(highestVal, root.val))
                dfs(root.right, max(highestVal, root.val))
        dfs(root, highest)
        return numGood