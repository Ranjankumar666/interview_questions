def knapsack0_1(w, v, W, n, dp ):
    '''
        kn(n, W)
        /    \ 
       /      \  
    kn(n-1, W) kn(n-1, W-wt[n])
    '''
    if W == 0 or n == 0:
        return 0
    
    if dp.get((n, W)):
        return dp[(n, W)]
    
    if w[n-1]  > W:
       return knapsack0_1(w[:n-1], v[:n-1], W, n-1, dp)

    
    dp[(n,W)] = max(v[n-1] + knapsack0_1(w[:n-1], v[:n-1], W -w[n-1], n-1, dp), knapsack0_1(w[:n-1], v[:n-1], W, n-1, dp))
    

    
    return dp[(n, W)]


w = [10 , 20, 30]
v = [60, 100, 120]
W = 50
dp =  {
    
}

print(knapsack0_1(w, v , W, len(w), dp))