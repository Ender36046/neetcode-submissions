"""
arr = []


"""

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[0] = 1
        for i in range(1, n+1):
            memo[i] = 0
            for step in [1,2]:
                subProblem = i - step
                if subProblem < 0: continue

                memo[i] = memo[i] + memo[subProblem]
        return memo[n]
