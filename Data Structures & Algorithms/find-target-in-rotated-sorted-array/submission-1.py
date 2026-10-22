class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def findMin(nums):
            l,r = 0, len(nums)-1
            while(l<r):
                if(r-l==1):
                    if(nums[r] > nums[l]):
                        return l
                    else:
                        return r
                mid = (l+r)//2
                if(nums[l] < nums[mid] and nums[r] < nums[mid]):
                    l = mid +1
                elif(nums[l] > nums[mid] and nums[r] > nums[mid]):
                    r = mid
                elif(nums[l] < nums[mid] < nums[r]):
                    return l
            return l

        def binarySearch(nums, t, offset = 0):
            l,r = 0, len(nums)-1
            while(l<r):
                mid = (l+r)//2
                if(nums[mid] > t):
                    r = mid-1
                elif(nums[mid] < t):
                    l = mid +1
                else:
                    return mid + offset
            if(l == r and nums[l] == t):
                return l + offset
            return -1

        minIndex = findMin(nums)

        print(minIndex)

        return max(binarySearch(nums[:minIndex], target), binarySearch(nums[minIndex:], target, minIndex))
