"""

Almost same as house robber 1,

but this time you can start anywhere on the circle

two possible ways, include or do not include last house

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums)<4):
            return max(nums)
        arrInclude = nums[1:len(nums)-2]
        arrNotInclude = nums[0:len(nums)-1]

        print(arrNotInclude)

        print(len(arrInclude))


        return max(self.dp(arrInclude) + nums[len(nums)-1], self.dp(arrNotInclude))
         
    def dp(self, numsDP):
        if(len(numsDP) <3):
            return max(numsDP)
        arr = [0]*len(numsDP)
        arr[0] = numsDP[0]
        arr[1] = max(numsDP[0], numsDP[1])
        for i in range(2,len(numsDP)):
            arr[i] = max(arr[i-2] + numsDP[i], arr[i-1])
            
        return arr[len(numsDP)-1]

        