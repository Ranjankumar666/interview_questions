def merge(arr, l, m , r):
    left =  [None]*(m - l+ 1 )
    right =[None]*(r - m )
    
    count = 0
    
    for i in range(m - l + 1):
        left[i] = arr[i]
    
    for i in range(r - m):
        right[i] = arr[i+m+ 1]
    
    i = 0
    j = 0
    k = l
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            
            count += (m + 1) - ( l + i )
            
    while( i < len(left)):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while( j < len(right)):
        arr[k] = right[j]
        j += 1
        k += 1

    return count

def counter(arr, start, end):
    res = 0
    
    if start < end:
        mid = start + (end- start)//2
        
        count += counter(arr, start, mid)
        count += counter(arr, mid+1, end)
        
        count += merge(arr, start, mid, end)