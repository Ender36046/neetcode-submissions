class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if(len(nums)<3):
            return nums[0]
        p0,p1 = 0,0
        seenAmount = {}
        seenValues = set()
        while True:
            p0 = nums[p0]
            p1 = nums[p1]
            p1 = nums[p1]
            if(nums[p0] == nums[p1]):
                p2 = 0
                while True:
                    if(nums[p0] == nums[p2]):
                        return nums[p0]
                    p0 = nums[p0]
                    p2 = nums[p2]


        return p0