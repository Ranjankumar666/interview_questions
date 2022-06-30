def fib(n):
    if n <= 1:
        return 1
    a = 0
    b =  1
    
    c = None
    i = 2
    while i <= n:
        c = a + b
        a = b
        b = c
        
        i += 1
    
    return c

print(fib(2)) 
    
    