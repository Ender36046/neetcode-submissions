"""

multiple possibilities = might be dp or greedy

Want to maximize distance, jump to biggest net distance gain

For example:

[2,4,2,0,0], want to jump to index 1 instead of index 2, since max distance for index 1 is index 5, and for index 2 its index 4

"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curIndex = 0
        while(curIndex < len(nums)):
            if(nums[curIndex] == 0):
                return (curIndex >= len(nums)-1)
            jump = 1
            bestJump = 1
            while(jump <= nums[curIndex] and jump+curIndex < len(nums)):
                if(nums[curIndex+bestJump]+bestJump < nums[curIndex+jump] +jump):
                    bestJump = jump
                jump+=1
            curIndex += bestJump
            print(curIndex)
        return (curIndex >= len(nums)-1)
