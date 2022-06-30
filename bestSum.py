def bestSum(target, arr, dp={}):
    if dp[target] is not None: return dp[target]
    if target == 0: return []
    if target < 0 :  return None
    
    
    shortest = None
    
    for i in arr:
        res  = bestSum(target - i, arr, dp)

        if res is not None:
            comb = res + [i]
            
            if shortest is None or len(shortest) > len(comb) :
                shortest = comb

    
    dp[target] = shortest
    return dp[target]

def bestSumTable(target, arr):
    table = [None for i in range(target + 1) ]
    
    table[0] = []
    
    for i in range(1, target + 1):
        for j in arr:
            idx = i - j
            
            if idx >= 0 and table[idx] is not None:
                curr = table[idx] + [j]
                if table[i] is None or len(table[i]) > len(curr):
                    table[i] = curr 
                    
    return table[target]

    
    
print("Memoization") 
print(bestSum(7, [5, 3, 4, 7], [None]*8))
print(bestSum(8, [2 ,3 ,5], [None]*9))
print(bestSum(8, [1 , 4, 5], [None]*9))
print(bestSum(100, [1, 2 ,5, 25], [None]*101))
print(bestSum( 39, [9 ,2 ,11 ,5 ,14 ,17 ,8 ,18],[None]*40))
    

print("Tabulization")  
print(bestSumTable(7, [5, 3, 4, 7]))
print(bestSumTable(8, [2 ,3 ,5]))
print(bestSumTable(8, [1 , 4, 5]))
print(bestSumTable(100, [1, 2 ,5, 25]))
print(bestSumTable( 39, [9 ,2 ,11 ,5 ,14 ,17 ,8 ,18]))