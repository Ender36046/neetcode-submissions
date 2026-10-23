# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        depth = 0
        listVals = []

        def sortLevels(root, depth):
            if(root != None):
                if(depth == len(listVals)):
                    listVals.append(root.val)
                sortLevels(root.right, depth+1)
                sortLevels(root.left, depth+1)
                

        sortLevels(root, depth)



        return listVals



            