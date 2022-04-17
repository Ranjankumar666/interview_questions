def maxIndexDiff(arr, n): 
    ##Your code here
    max_i = 0
    i = 0
    j  = n - 1

    while i < j:
        if arr[i] <= arr[j] and (j-i) > max_i:
            max_i = j - i
            j = n- 1
        else:
            j -= 1
            i += 1
        
    return max_i

arr = [97, 65, 24, 84, 10, 82, 2, 51, 1, 91, 62, 59, 80, 76, 26, 66, 11]
print(maxIndexDiff(arr,len(arr)))