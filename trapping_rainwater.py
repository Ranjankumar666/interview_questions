def get(arr, start, end):
    m = 0

    for i in range(start, end):
        if arr[i] > m:
            m = arr[i]
    return m
    
''''
    # eq: current_cpacity = min(maxL, maxR) - curr_height 
    # use two pointers
    # chose the smallest one as current height
    # if greater maxL | maxR ( depending upon which pointer is small) updated and move
    # else update total height += naxL | maxR - arr[p1 | p2]
'''

def soln_v2(arr):
    n = len(arr)

    p1 = 0
    p2 = n - 1

    total = 0
    maxL = 0
    maxR = 0

    while p1 < p2 :

        if arr[p1] < arr[p2]:
            if arr[p1] > maxL:
                maxL = arr[p1]
            else:
                total += maxL - arr[p1]               
            p1+= 1
        else:
            if arr[p2] > maxR:
                maxR = arr[p2]
            else:
                total += maxR - arr[p2]
            p2 -= 1

    return total
    
            
def solution(arr):
    n = len(arr)

    total = 0

    for i in range(1, n-1):
        l1 = get(arr, 0, i)
        l2 = get(arr, i+1, n)


        h = min(l1,l2) - arr[i]
        if h >= 0:
            total += h
            
    
    return total
            
print(soln_v2([7, 4, 0, 9]))