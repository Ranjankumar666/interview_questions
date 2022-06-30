def ls(arr):
    arr = sorted(arr)
    
    global_max = 0
    temp = 0
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]: continue
            
        elif arr[i+1] - arr[i] == 1: temp += 1
            
        else:
            global_max = max(temp , global_max)
            temp =0
            
    global_max = max(global_max , temp)
    
    return global_max+1



print(ls ([0,3,7,2,5,8,4,6,0,1]))
print(ls([3,-1,0,5,6, 4]))
