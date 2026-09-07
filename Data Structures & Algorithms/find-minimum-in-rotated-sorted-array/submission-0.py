class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        while l < r:
            if(r-l==1):
                return min(nums[r],nums[l])
            mid = (l+r)//2
            if(nums[l] < nums[mid] and nums[r] < nums[mid]):
                l = mid +1
            elif(nums[l] > nums[mid] and nums[r] > nums[mid]):
                r = mid
            elif(nums[l] < nums[mid] < nums[r]):
                return nums[l]
        return nums[l]