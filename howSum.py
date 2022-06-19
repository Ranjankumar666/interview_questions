def howSum(target, arr,dp = {},  curr= []):
    
    if target in dp:
        return dp[target]
    
    if target == 0:
        return curr
    
    for i in arr:
        if i <= target  and  howSum(target - i, arr, dp, curr) is not None:
            curr.append(i)
            dp[target] = curr
            return curr
    
    dp[target]= None
    return None


print(howSum(7, [1 , 1, 2]))