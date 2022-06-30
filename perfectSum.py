def getTotal(arr, k, s, dp = {}):
    key = (k, sum)

    if key in dp: dp[key]
    
    if s == 0:
        return 1
    if k == 0 and s != 0:
        return 0
    
    if s < 0:
        return 0
    
    count = 0
    

    count += getTotal(arr, k -1 ,s - arr[k-1])
    count += getTotal(arr, k - 1,   s )
    
    
    dp[key] = count
    return count
           
       
    
    
print(getTotal([2, 3, 5, 6, 8, 10], 6, 10))
print(getTotal([1, 2, 4,3, 5], 5, 10))
print(getTotal([9, 7, 0, 3, 9 ,8, 6, 5, 7, 6], 10, 31))
print(getTotal([ 5, 6,  7,  8,  9], 5, 12))
print(getTotal([9, 5, 7, 2, 5, 1], 6, 23))