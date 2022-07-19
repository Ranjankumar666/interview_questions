from math import ceil, floor
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        
        
        while left <= right:
            mid = left + (right - left)//2
            
            if mid + 1< n and nums[mid+1] < nums[mid]:
                return nums[mid+1]

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
            
        return nums[0]
           

    
s = Solution()

print(s.findMin([2 ,3 ,4, 5,1 ]))
print(s.findMin([3 ,4, 5,1, 2 ]))
print(s.findMin([4,5,1,2,3]))
print(s.findMin([284,287,289,293,295,298,0,3,8,9,10,11,12,15,17, 20, 21]))
