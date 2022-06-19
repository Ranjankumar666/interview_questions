import math


def oI(n):
    return int(math.modf(n)[1])
    
def solution(num, dp):

    if num <= 7:
        return num

    if dp.get(num) :
        return dp[num]
        
    res  = solution(oI(num/2), dp) + solution(oI(num/3), dp) + solution(oI(num/4), dp)
    
    dp[num] = res
    return dp[num]

n = 24

print(solution(n, {}))