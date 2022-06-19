
def solution2(cost,):
    memo =[None]*len(cost)

    memo[0] = cost[0]
    memo[1] = cost[1]

    for k in range(2, len(cost)):
        memo[k] = cost[k] + min(memo[k-1], memo[k-2])
    
    return memo.pop()


def solution(cost, i, memo):
    if i < 0: return 0
    if i == 0 or i == 1:
        return cost[i]

    if memo[i] : 
        return memo[i]

    memo[i] = cost[i] + min(solution(cost, i-1, memo), solution(cost, i-2, memo))
    return memo[i]

def minCost(cost):

    # return min(solution(cost, n-1, memo), solution(cost, n-2, memo))
    return solution2(cost)
    
cost = [1,100,1,1,1,100,1,1,100,1]
# cost = [20 ,15, 30, 5]
# cost = [10 ,15, 20]

print(minCost(cost))
