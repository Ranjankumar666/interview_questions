def peakElement(arr, n):
    # Code here
    
    left = -1
    right = 1
    
    for i in range(n):
        curr = arr[i]
        isPeak = False
        
        if left == -1 or curr > arr[left]:
            if (right == n) or curr > arr[right]:
                isPeak = True

        if isPeak:
            return i
        
        left += 1
        right += 1
            
    
    return -1

arr = [1 ,2 ,3]
print(peakElement(arr , len(arr)))