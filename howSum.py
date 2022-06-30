def howSum(target, arr,dp = {}):
    
    if target in dp:
        return dp[target]
    
    if target == 0:
        return []
    
    for i in arr:
        if i <= target :
            res = howSum(target - i, arr, dp)
            
            if res is not None:
                comb = res + [i]
                dp[target] = comb
                return comb
    
    dp[target]= None
    return None

def howSumTable(target, arr):
    table = [None for i in range(target+1)]
    table[0] = []
    
    for i in range(1, target+1):
        for j in arr:
            idx = i - j
            
            if idx >= 0 and table[idx] is not None:
                table[i] = table[idx] + [j]
                break

    return table[target]

def howSumTable2(target, arr):
    table = [None for i in range(target+1)]
    table[0] = []
    
    for i in range(target+1):
        if table[i] is not None:
            for j in arr:
                idx = i + j
                
                if idx < target+1:
                    table[idx] = table[i] + [j]
    
    return table[target]



print(howSum(300, [7, 14]))
print(howSumTable(7 , [3 ,5,4, 7]))
print(howSumTable(7 , [2, 4]))
print(howSumTable(18, [5, 3, 1,7]))
print(howSumTable(300, [7 , 14]))

print(howSumTable2(7 , [3 ,5,4, 7]))
print(howSumTable2(7 , [2, 4]))
print(howSumTable2(18, [5, 3, 1,7]))
print(howSumTable2(300, [7 , 14]))