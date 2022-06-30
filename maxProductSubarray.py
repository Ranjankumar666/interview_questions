def maxProductSubArray(arr, i =0):
    N = len(arr)
    if i == N -2:
        return max(arr[0], arr[1], arr[0]*arr[1])
    if i == N - 1:
        return arr[0]
    
    
    
    res = maxProductSubArray(arr, i+1)

    return max(res, res*arr[i], arr[i])


print(maxProductSubArray([6 , -3, -10, 0 , 2 ]))
print(maxProductSubArray([-8, -6, -1]))
print(maxProductSubArray([2, 3, 4, 5, -1, 0]))