def partition(arr, left, right):
    pivot = arr[right]
    pIndex = left

    for curr in range(left, right+1):
        if arr[curr] > pivot:
            arr[curr], arr[pIndex] = arr[pIndex], arr[curr]
            pIndex += 1
        
    arr[pIndex],arr[right] = arr[right], arr[pIndex]

    return pIndex


def quickSelect(arr,left, right,  k):


    p = partition(arr, left, right)

    if p == k:
        return arr[p]
    elif k < p:
        return quickSelect(arr, left, p-1, k)
    else:
        return quickSelect(arr, p+1, right , k)

def findKThLargest(arr, k):
    n = len(arr)
    target = k-1

    return quickSelect(arr, 0 , n-1 ,target)

arr = [5,3,1,6,4,2]
toFind = 1
print(findKThLargest(arr, toFind))