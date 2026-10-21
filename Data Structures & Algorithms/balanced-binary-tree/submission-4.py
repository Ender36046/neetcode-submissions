# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if root == None:
                return [True, 1]

            else:
                leftRes = dfs(root.left)
                rightRes = dfs(root.right)

                if(leftRes[0] == False or rightRes[0] == False or abs(leftRes[1] - rightRes[1]) > 1):
                    return [False, -1]

                else:
                    return [True, 1+ max(leftRes[1], rightRes[1])]

        return dfs(root)[0]

                
