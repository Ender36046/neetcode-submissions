# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isIdentical(self, root1, root2):
        if(root1 == None and root2 == None):
            return True

        if(root1 == None and root2 != None):
            return False
        elif(root1 != None and root2 == None):
            return False
        
        leftSame = self.isIdentical(root1.left, root2.left)

        rightSame = self.isIdentical(root1.right, root2.right)

        return (leftSame and rightSame and root1.val == root2.val)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(root == None and subRoot != None):
            return False
        elif(root != None and subRoot == None):
            return False
        if(root.val == subRoot.val):
            return (self.isIdentical(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        else:
            return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
