def moveZeros(nums):
    order = [ i for i in nums if i != 0]
            
    i = 0
    
    while i < len(order):
        nums[i] = order[i]
        i += 1
        
    
    while i < len(nums):
        nums[i] = 0
        i += 1
                
nums = [0,1,0,3,12]
moveZeros(nums)
print(nums)