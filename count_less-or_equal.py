def bS(arr, k):
    n = len(arr)
    j = n-1

    if k > arr[n-1]:
        return n

    while j > -1:
        if arr[j] <= k:
            return j+1

        j -= 1

    return -1

def countEleLessThanOrEqual(arr1,n1,arr2,n2):
    #returns the required output

    arr2 = sorted(arr2)
    res= []
    for i in range(n1):
        p = bS(arr2, arr1[i] )
        
        if p != -1:
            res.append(p)
        
    
    return res

m = 6
n = 6
arr1 = [1,2,3,4,7,9]
arr2 = [0,1,2,1,1,4]
print(countEleLessThanOrEqual(arr1, m, arr2, n))