def soln(S, val, idx, dp={}):
    key = (val, idx)
    if (val, idx) in dp: return dp[(val, idx)]
    
    if  val < 0: return 0
    if val == 0 : return 1
    if idx >= len(S): return 0
    

 
    count = soln(S, val - S[idx] ,  idx) + soln(S, val ,  idx+1)
    dp[(val, idx)] = count 
    
    return count





print(soln([1 , 2,3], 4, 0))