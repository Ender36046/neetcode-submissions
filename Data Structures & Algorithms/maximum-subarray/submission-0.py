class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        biggestSum = nums[0]
        currentSum = nums[0]
        for i in nums[1:]:
            if(currentSum < 0):
                currentSum = 0
            currentSum +=i
            if(currentSum > biggestSum):
                biggestSum = currentSum
        return biggestSum