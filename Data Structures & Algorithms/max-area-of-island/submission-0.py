class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        explored = {}
        biggestIsland = 0
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                explored[(i,j)] = 0

        def bfs(position):
            nonlocal biggestIsland
            queue = deque()
            queue.append(position)
            islandSize = 0
            while queue:
                currPos = queue.popleft()
                if(explored[currPos] == 0):
                    explored[currPos] = 1
                    islandSize +=1
                    biggestIsland = max(islandSize, biggestIsland)
                    currX = currPos[0]
                    currY = currPos[1]
                    if(currX -1 >= 0 and grid[currY][currX-1] == 1):
                        queue.append((currX-1,currY))
                    if(currX + 1 < len(grid[0]) and grid[currY][currX+1] == 1):
                        queue.append((currX+1, currY))
                    if(currY -1 >= 0 and grid[currY-1][currX] == 1):
                        queue.append((currX,currY-1))
                    if(currY +1  < len(grid) and grid[currY+1][currX]==1):
                        queue.append((currX, currY+1))  

        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if(explored[(i,j)] == 0 and grid[j][i] == 1):
                    bfs((i,j))
        return biggestIsland
