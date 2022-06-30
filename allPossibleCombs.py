def changeCoinsCombination(coins, amt, dp= {}):
    

    
    if amt in dp:
        return dp[amt]
    if amt == 0:
        return [[]]
    
    if amt < 0:
        return []
    
    allWays =[]
    
    for coin in coins:
        ways = changeCoinsCombination(coins, amt - coin, dp)
        targetWays = list(map(lambda x: [coin] + x, ways ))
        allWays = allWays + targetWays
       
    dp[amt] = allWays 
    return allWays


print(changeCoinsCombination([1 ,2 , 3], 4))