def sum3Dictonary(arr):  
    if len(arr) < 3:
        return []
    
    # arr = sorted(arr)
        
    res = []

    for i in range(len(arr)):
        if i != 0 and arr[i-1] == arr[i]: continue
         
        target = -arr[i]
        dp = {}
        
        j = i + 1
        
        while j < len(arr):
            t = target - arr[j] 
#                 dp[t] is k
            if t in dp :
                k = dp[t]
                res.append([arr[i], arr[j], arr[k]])
                
                while j+1 < len(arr) and arr[j] == arr[j+1] :
                    j += 1
            else:
                dp[arr[j]] = j
            
            j += 1
            
                    
    return res   


def sum3TwoPointers(arr):
    arr = sorted(arr)
    res = []
    
    for i in range(len(arr)):
        if i != 0 and arr[i-1] == arr[i]: continue
        
        j = i+1
        k = len(arr) - 1
        
        while  j < k:
            s = arr[i]+ arr[j] + arr[k]
            
            if s == 0:
                res.append([arr[i], arr[j], arr[k]])
                j += 1
                
                while j < k and arr[j-1] == arr[j]: j += 1
            elif s < 0:
                j += 1
            else:
                k -= 1
        
    return res

print(sum3Dictonary([0, 0,0 ,0 ]))
print(sum3Dictonary([1, 2,-2, -1]))
print(sum3TwoPointers([0, 0,0 ,0 ]))
print(sum3TwoPointers([1, 2,-2, -1]))