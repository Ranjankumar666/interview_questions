def lower(arr, left, right, k):
    if left <= right:
        m = left + (right - left)//2
        if arr[m] == k:
            if (m == 0 or arr[m-1] != k):
                return m
            else:
                return lower(arr, left, m-1, k)
        
        elif arr[m] < k:
            return lower(arr, m+1, right, k)
        else:
            return lower(arr, left , m-1, k)
    
    return -1

        
def upper(arr,left , right, k ):
    if left <= right:
        m = left + (right - left)//2
        if arr[m] == k:
            if (m == len(arr) - 1 or arr[m+1] != k):
                return m
            else:
                return upper(arr, m+1, right, k)
        
        elif arr[m] < k:
            return upper(arr, m+1, right, k)
        else:
            return upper(arr, left , m-1, k)
    
    return -1
arr = [1 , 3, 3, 3, 5]

print(lower(arr, 0, len(arr)-1, 3))
print(upper(arr, 0 , len(arr) -1 , 3))
