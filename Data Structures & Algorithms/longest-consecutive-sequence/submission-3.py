class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <1: return 0
        hashSet = set(nums)
        biggest = 0
        for i in hashSet:
            if(not i -1 in hashSet):
                tempCount = 0
                while i in hashSet:
                    tempCount +=1
                    biggest = max(biggest, tempCount)
                    i+=1
        return (biggest)

