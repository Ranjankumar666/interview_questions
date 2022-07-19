from typing import List


def minCost( n: int, cuts: List[int]) -> int:

    def dfs(i, j):
        if abs(j - i) == 1:
            return 0
        if j <= i :
            return 0

        minVal = float('inf')
        for c in range(len(cuts)):
            p  = ( j -i ) + min(dfs(i, cuts[c]), dfs(cuts[c], j))
            minVal = min(p, minVal)
            
        
        return minVal
        
    
    minVal = float('inf')
    for i in range(len(cuts)):
        p = cuts[i] + min(dfs(0, i), dfs(i, len(cuts)))
        minVal = min(p , minVal)
    
    return minVal


print(minCost(7, [1 , 5]))