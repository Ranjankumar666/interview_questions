
def canSum(target, arr, dp= {}):
    
    if dp.get(target) is not None:
        return dp[target]
      
    if target == 0:
        return True
    
    for i in arr:
        if i <= target  and canSum(target - i , arr, dp):
            dp[target] = True
            return True
        
    dp[target] = False
    return False

def canSumTable(target, arr):
    table = [[False for i in range(len(arr))] for j in range(target + 1)]
    
    for i in range(target + 1):
        for j in range(len(arr)-1 , -1 , -1):
            if i == 0:
                table[i][j] = True
            else:
                nTarget = i - arr[j]
        
                if nTarget >= 0 and table[nTarget][j] is True:
                    table[i][j] = True
                
                elif j + 1 < len(arr) and table[i][j+1] is True:
                    table[i][j] = True
                else:
                    table[i][j] = False            
    
    return table[target][0]


def canSumTable2(target, arr):
    table = [ False for i in range(target + 1)]
    
    table[0] = True
    combs = []
    for t in range(1, target+1):
        s = []
        for num in arr:
            idx = t - num
            
            res = False
            
            if idx >= 0:
                res = table[idx]
    
            table[t] = res
            
            if res:
                s.append(num)
        combs.append(s)
        
    print(table)
    return combs


'''
   table = [ False for i in range(target + 1)]
    
   table[0] = True 
   
   for i in range(target+1):
        if(table[i]):
            for num in S:
                if i + num < n+ 1:
                    table[i + num] = True
    
   return table[target] 
'''


print(canSum(7, [  2 , 4]))
print(canSumTable2(7 , [2 , 4]))

    
    