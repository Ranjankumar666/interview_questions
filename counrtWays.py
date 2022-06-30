def countWays(n):

    a = 0
    b = 1
    
    c = None
    
    i = 2
    while i <= n+1 :
        c = a + b
        
        a = b
        b = c
        i += 1
        
    return c

print(countWays(6))