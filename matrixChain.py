def solution(arr, i, j, dp):

 
    if dp[i][j]:
        return dp[i][j]
    
    if i == j :
        dp[i][j] = 0
        return 0 

    
    mini = float('inf')
    for k in range(i, j):
        
        count = solution(arr, i, k, dp) + solution(arr, k+1, j, dp) + arr[i-1]*arr[k]*arr[j]
    
        
        mini = min(mini, count)
    
    dp[i][j] = mini
    
    return dp[i][j]


arr = [10, 20, 30, 40]
n = len(arr)
dp = [[None for i in range(n)] for j in range(n)]

print(solution(arr, 1, n-1, dp))