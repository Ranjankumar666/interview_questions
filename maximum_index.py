def solution( arr, n): 
        ##Your code here
        max_i = 0
        left = 0
        right  = n - 1
    
        while left < right :
            
            if arr[left] <= arr[right]:
                max_i = max(max_i, (right - left))
            
            if arr[left + 1] < arr[right] or arr[left] > arr[right]:
                left += 1
            else:
                right -= 1
            
        return max_i
#15 86 78 93 100 6
arr = list(map(int , "92 71 39 88 3 24 33 46 24 6 31 54 65".split(" ")))

print(solution(arr, len(arr)))