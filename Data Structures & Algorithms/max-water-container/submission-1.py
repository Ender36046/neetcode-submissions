"""

area = lxw

l = r-l

w = min(heights[r], heights[l])

"""


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        bestl,bestr = 0,0
        while(l<=r):
            if((r-l)*min(heights[r],heights[l]) > (bestr-bestl)*min(heights[bestl],heights[bestr])):
                bestl, bestr = l,r
            if(heights[r] > heights[l]):
                l+=1
            else:
                r-=1
        return (bestr-bestl)*min(heights[bestl],heights[bestr])
            