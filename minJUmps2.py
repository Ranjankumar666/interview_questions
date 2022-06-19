def minJumpsSolution(arr: list[any], i: any, dp: list[any]):
    if i >= len(arr)-1:
        return 0
    
    if arr[i] == 0:
        return -1

    if dp[i] is not None:
        return dp[i]
    

    jumps = arr[i+1]
    
    minimum = float('inf')
    
    for j in range(1, jumps+1):
        curr = minJumpsSolution(arr, i+j, dp)
        
        if curr != -1 and curr + 1 < minimum:
            minimum = curr + 1
    
    dp[i] = minimum
    
    return dp[i]
            
        
arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
n = len(arr)
dp = [None]*len(arr)
print(minJumpsSolution(arr, 0, dp))