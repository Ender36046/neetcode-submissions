# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(root1, root2):
            root1val, root2val = 0,0
            if(root1 == None and root2 == None):
                return True
            if(root1 == None):
                root1val = None
            else:
                root1val = root1.val

            if(root2 == None):
                root2val = None
            else:
                root2val = root2.val

            if(root1val == root2val):
                return (dfs(root1.left, root2.left) and dfs(root1.right, root2.right))
            else:
                return False

        return dfs(p,q)