def partition(arr, left, right):
    pivot = arr[right]
    pIndex = left 

    for i in range(left, right):
        if arr[i] < pivot:
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex += 1
    
    arr[pIndex], arr[right] = arr[right], arr[pIndex]
    return pIndex


arr = [2,8, 6, 0, 7]

partition(arr, 0 , 3)
print(arr)