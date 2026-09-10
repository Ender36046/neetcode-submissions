"""

multiple possibilities = might be dp or greedy

Want to maximize distance, jump to biggest net distance gain

For example:

[2,4,2,0,0], want to jump to index 1 instead of index 2, since max distance for index 1 is index 5, and for index 2 its index 4

"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curIndex = 0
        for i in range(len(nums)):
            if i > curIndex:
                return False
            curIndex = max(curIndex, i + nums[i])
        return curIndex >= len(nums)-1
