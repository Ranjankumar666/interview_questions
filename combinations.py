

def make( k, nums, size):
    N = len(nums)
    
    if N == size:
        return [[]]
    
    i = k + 1

    allWays = []
    while i < len(nums):

        res = make(i+1, nums, size )
        res = list(map(lambda x: x + nums[i+1], res))
        allWays += res
        
        i += 1
        
    return allWays
        

def combinations(nums,  s ):
    
    combs = []
    for i in range(len(nums)):
        combs += make([], i, nums, s) 
        
    if len(combs) == 0:
        return combs
    
    if isinstance(combs[0], int):
        return [combs]
    
    return combs

print(combinations([1, 2, 3], 1))
    
    
    
    