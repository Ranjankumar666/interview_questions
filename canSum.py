
def canSum(target, arr, dp):
    
    if dp.get(target) is not None:
        return dp[target]
      
    if target == 0:
        return True
    
    for i in arr:
        if i <= target  and canSum(target - i , arr, dp):
            dp[target] = True
            return True
        
    dp[target] = False
    return False


canSum(10, [  3, 2, 1], {})

    
    