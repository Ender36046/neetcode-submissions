class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix)-1
        while l != r:
            if(r-l ==1):
                value = matrix[r][0]
                if(value > target):
                    return self.binarySearch(matrix[l],target)
                else:
                    return self.binarySearch(matrix[r],target)
            midArr = (l+r)//2
            value = matrix[midArr][0]
            if(target > value):
                l = midArr
            elif(target < value):
                r = midArr-1
            elif(target == value):
                return True
            
        return self.binarySearch(matrix[l], target)


    def binarySearch(self,arr, num):
        l,r = 0, len(arr)-1
        while l<=r:
            mid = (l+r)//2
            if(arr[mid] == num):
                return True
            elif(num < arr[mid]):
                r = mid -1
            else:
                l = mid+1
        return False