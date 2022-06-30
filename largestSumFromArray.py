def maker(a, arr):
    s = ''
    for i in reversed(arr):
       s += str(i)
        
    s += str(a)
    
    return s

def largestSumFromArray(arr):
    arr = sorted(arr)
    max_ = -float('inf')
    
    for i in range(len(arr)):
        remainder = arr[:i] + arr[i+1:]
        res = int(maker(arr[i] , remainder))
        
        max_ = max(res, max_)
        
    return max_



print(largestSumFromArray([3, 30, 34, 5, 9]))