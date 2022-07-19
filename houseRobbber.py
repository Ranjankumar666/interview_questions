def rob(nums, i=0):
    if i == len(nums) - 1 or i +1 == len(nums) - 1: 
        return nums[i]

    
    maximum = -float('inf')
    
        
    for k in range(i+2, len(nums)):
        curr = nums[i] + rob(nums, k)
        maximum = max(maximum, curr)    
        
    
    return maximum
    
    
    


print(rob([1 ,2, 3, 1]))
# print(rob([2,7,9,3,1]))