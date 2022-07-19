def breakNumber(n, nums, i):
    # Write your code here.
    if n == 0:
        return [[]]

    if n < 0:
        return []

    
    res = []
    
    for k in range(i , len(nums)):
        p = breakNumber(n - nums[k], nums, k)
        p = list(map(lambda x : x + [nums[k]], p))
        res += p
    
    return res
    


print(breakNumber(4, [ i for i in range(1, 4) ], 0))