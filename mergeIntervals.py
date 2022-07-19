from typing import List

def merge(arr: List[List[int]]) -> List[List[int]]:
    n = len(arr)
    j = 0
    
    for i in range(1, n):
        p,q = arr[i]
        k, l = arr[j]
        
        
        
        if l >= p and l < q:
            merged = [k , q]
            arr[i] = merged
            j += 1
        
        
    return arr[1:]


print(merge( [[1,3],[2,6],[8,10],[15,18]]))