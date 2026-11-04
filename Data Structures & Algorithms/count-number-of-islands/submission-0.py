class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        explored = {}
        currPos = (0,0)
        numIslands = 0
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                explored[(i,j)] = 0

        def bfs(position):
            queue = deque()
            queue.append(position)
            while queue:
                currPos = queue.popleft()
                if(explored[currPos] == 0):
                    explored[currPos] = 1
                    currX = currPos[0]
                    currY = currPos[1]
                    if(currX -1 >= 0 and grid[currY][currX-1] == "1"):
                        queue.append((currX-1,currY))
                    if(currX + 1 < len(grid[0]) and grid[currY][currX+1] == "1"):
                        queue.append((currX+1, currY))
                    if(currY -1 >= 0 and grid[currY-1][currX] == "1"):
                        queue.append((currX,currY-1))
                    if(currY +1  < len(grid) and grid[currY+1][currX]=="1"):
                        queue.append((currX, currY+1))  

        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if(explored[(i,j)] == 0 and grid[j][i] == "1"):
                    numIslands +=1
                    bfs((i,j))
        return numIslands
