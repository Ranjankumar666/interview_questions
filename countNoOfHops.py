count = 0 
def solution(pos, n, dp):
    if pos == n:
       return 1
    if pos > n:
        return 0
    if dp[pos]:
        return dp[pos]

    total = 0
    for i in range(1, 4):
        total += solution(pos+i, n, dp)

    dp[pos] = count
    
    return dp[pos]


n = 5
dp = [False]*(n+1)
solution(0, n, dp)

print(count)