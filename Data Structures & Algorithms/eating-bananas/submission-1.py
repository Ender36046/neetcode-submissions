class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h ==len(piles):
            return max(piles)
        maxVal = max(piles)
        lowestRate = 1
        maxRate = maxVal
        while(lowestRate < maxRate):
            testRate = (maxRate+lowestRate)//2
            totalTime = 0
            for i in piles:
                totalTime += math.ceil(i/testRate)
            if totalTime > h:
                lowestRate = testRate +1
            elif totalTime <= h:
                maxRate = testRate
        return maxRate