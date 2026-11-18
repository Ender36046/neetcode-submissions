class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        stack = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    stack.append((i,j))
        minute = 0
        while stack:
            tempStack = deque()
            for i in range(len(stack)):
                curr = stack.popleft()
                currRow = curr[0]
                currCol = curr[1]
                if (grid[currRow][currCol] == 1) or (grid[currRow][currCol] == 2 and minute == 0):
                    if currRow > 0:
                        tempStack.append((currRow-1, currCol))
                    if currRow < len(grid)-1:
                        tempStack.append((currRow+1, currCol))
                    if currCol > 0:
                        tempStack.append((currRow, currCol-1))
                    if currCol < len(grid[0])-1:
                        tempStack.append((currRow, currCol +1))
                    if grid[currRow][currCol] == 1:
                        grid[currRow][currCol] = 2
            minute +=1
            stack.extend(tempStack)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return max(minute-2,0)