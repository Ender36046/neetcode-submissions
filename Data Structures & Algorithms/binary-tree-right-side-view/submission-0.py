# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        listOfLevels = []
        depth = 0

        def sortLevels(root, depth):
            if(root != None):
                if(depth > len(listOfLevels)-1):
                    listOfLevels.append([])
                listOfLevels[depth].append(root.val)
                sortLevels(root.left, depth+1)
                sortLevels(root.right, depth+1)

        sortLevels(root, depth)

        listVals = []
        for i in listOfLevels:
            listVals.append(i[-1])

        return listVals



            