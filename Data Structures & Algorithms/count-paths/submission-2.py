class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        numWays = {}
        numWays[(0,0)]= 1
        def DP(curX, curY):
            for curX in range(n):
                for curY in range(m):
                    if(curX > 0 or curY > 0):
                        numWays[(curX,curY)] = numWays.get((curX-1,curY),0) + numWays.get((curX,curY-1),0)

        DP(0,0)

        return numWays[(n-1,m-1)]