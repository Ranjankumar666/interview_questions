def gridTraveller(m, n , dp):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n== 1: 
        return 1
    
    if dp.get((m, n)):
        return dp[(m, n)]
    
    count = 0
    
    count += gridTraveller(m-1, n, dp)
    count += gridTraveller(m, n-1, dp)
    
    dp[(m , n)] = count
    
    return dp[(m , n)]

print(gridTraveller(18 , 18, {}))