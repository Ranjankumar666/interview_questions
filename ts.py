def solution(arr, t):
    mapper = {}
    res = []
    
    for i, e in enumerate(arr):
 
        if mapper.get(e) is None:
            mapper[t-e] = i
        
        else: 
            res.append((mapper[e], i))
            mapper[t - e] = i
    
    return res


arr = [1, 4, 6, 2, 3, 2]
print(solution(arr, 10))