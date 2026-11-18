class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        stack = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    stack.append((i,j))
        level = 0
        while stack:
            tempStack = deque()
            for i in range(len(stack)):
                curr = stack.popleft()
                currRow = curr[0]
                currCol = curr[1]
                if (grid[currRow][currCol] == 2147483647) or (grid[currRow][currCol] == 0 and level == 0):
                    if currRow > 0:
                        tempStack.append((currRow-1,currCol))
                    if currRow < len(grid)-1:
                        tempStack.append((currRow+1, currCol))
                    if currCol > 0:
                        tempStack.append((currRow, currCol-1))
                    if currCol < len(grid[0]) -1:
                        tempStack.append((currRow, currCol+1))
                    if(grid[currRow][currCol] > level):
                        grid[currRow][currCol] = level
            stack.extend(tempStack)
            level+=1