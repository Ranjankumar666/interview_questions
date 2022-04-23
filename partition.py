def partition(arr, left, right):
    pivot = arr[right]
    pIndex = left 

    for i in range(left, right):
        if arr[i] < pivot:
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex += 1
    
    arr[pIndex], arr[right] = arr[right], arr[pIndex]
    return pIndex


def quickSort(arr, left ,right):

    if left < right:
        pivot = partition(arr, left, right)
        quickSort(arr, left, pivot -1)
        quickSort(arr , pivot + 1, right)


arr = [2,8, 6, 0, 7]

quickSort(arr, 0, len(arr) -1)
print(arr)