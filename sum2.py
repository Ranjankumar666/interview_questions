def sum2(arr, target):
    
    dp = {}
    dp[arr[0]] = 0
    res = []
    
    
    for i in range(1, len(arr)):
        j = target - arr[i] 
        
        if j in dp:
            res.append([arr[i], arr[dp[j]]])
            
        
        dp[arr[i]] = i
       
    return res


print(sum2([-1,0,1,2,-1,-4], 0))