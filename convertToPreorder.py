import math


def toPreorder(arr,left, right, res):
    if left <= right:
        mid = math.ceil((right + left)/2)
        
        res.append(arr[mid])
        toPreorder(arr, left, mid-1, res )
        toPreorder(arr, mid+1, right, res)
        
    
    return res

arr = range(1, 8)
print(toPreorder(arr, 0, len(arr) -1, []))