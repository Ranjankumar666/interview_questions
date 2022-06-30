
def combs(arr):
    n = len(arr)
    res = []
    curr = []
    
    def dfs(i):
        if i >= len(arr):
            res.append(curr[:])
            return 
        
        curr.append(arr[i])
        dfs(i+1)
        
        curr.pop()
        dfs(i+1)
        
    dfs(0)
    
    return res
        
print(combs([1 ,2 ,3]))