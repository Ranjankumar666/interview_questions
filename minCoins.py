def minCoins(coins,  V, dp):
    if V in dp:
        return dp[V]
    if V == 0:
        return []
    if V < 0 :
        return None
    
    shortest = None
    
    for coin in coins:

        res =  minCoins(coins,  V - coin, dp) 
        if res is not None:
            comb = res + [coin]
            
            if shortest is  None or  len(comb) < len(shortest):
                shortest = comb
                
    dp[V] = shortest
            
    return shortest
    

print(minCoins([9 ,2 ,11 ,5 ,14 ,17 ,8 ,18], 39, {}))

        
            