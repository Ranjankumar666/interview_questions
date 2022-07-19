from math import sqrt


def numSquares(n, dp):
    if n in dp: return dp[n]
    if n < 4:
        return n


    
    shortest = float('inf')
    for i in range(round(sqrt(n)), 0 , -1):
        newTarget = n - i*i
        
        if newTarget >= 0:
            curr = 1 + numSquares(newTarget, dp)
            shortest = min(curr, shortest)
    
    dp[n] = shortest
    return shortest


print(numSquares(10, {}))
print(numSquares(13, {}))