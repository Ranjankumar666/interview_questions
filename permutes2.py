from collections import Counter

def permute_2(arr):
    res = []
    perm = []
    count = Counter(arr)
    
    def dfs():
        if len(perm) == len(arr):
           res.append(perm[:])
            
        
        for k in count:
            if count[k] > 0:
                perm.append(k)
                count[k] -= 1
                
                dfs()
                
                perm.pop()
                count[k] += 1
                            
                
    dfs()
    
    return res


print(permute_2([1, 1, 2,]))
    
    