def _permute(curr, arr, results):
    if len(curr) == len(arr):
        results.append(curr)
        return results

    for i in arr:
        if i not in curr:
            _permute(curr+[i], arr, results)
    
    return results

        
    
    
    
def permute(arr):
    return _permute([], arr, [])


def permute_bcaktrack(arr):
    
    if  len(arr) == 1:
        return [arr[:]]
    
    print(arr)
    res = []
    for _ in range(len(arr)):
        n = arr.pop(0)
       
        p = permute_bcaktrack(arr)
        
        for pt in p:
            pt.append(n)
        
        # print(p)
        res += p
        arr.append(n)
        
        
    return res 

# print(permute([1, 2, 3]))
print(permute_bcaktrack([1 ,2 , 3]))