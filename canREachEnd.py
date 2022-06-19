def solution(i, A, dp):

    if i == len(A) - 1:
        return True
        
    if A[i] == 0:
        return False

    if dp[i]: 
        return dp[i]
    
    rng = A[i]
    for j in range(rng, 0, -1):
       
        if i +j < len(A):
            res = solution(i+j, A, dp) 
            dp[i+j] = res

            if res:
                return True
        
       
            
    return False


A = [1, 2, 0, 3, 0, 0]
dp = [None]*len(A)
print(solution(0, A, dp))