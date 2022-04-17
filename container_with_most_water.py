import heapq


def soln(arr):
    max_w = 0

    for p1 in range(len(arr)):
        for p2 in range(p1+1,len(arr)):
            h = min(arr[p1], arr[p2])
            w = p2 - p1

            if h*w > max_w:
                max_w = h*w
    return max_w

'''
    Increment or Decrement min value pointer
'''
def solution(arr):
    max_w = 0
    
    p1 = 0
    p2 = len(arr) - 1


    while p1 < p2:
        h = min(arr[p1], arr[p2])
        w = abs(p1 -p2)

        if(h*w > max_w):
            max_w = h*w 

        if arr[p1] < arr[p2]:
            p1 += 1
        else:
            p2 -= 1

         

    return max_w

arr_str = '91 4 2 53 92 82 21 16 18 95 47 26 71 38 69 12 67 99 35 94 3 11 22 33 73 64 41 11 53 68 47 44 62 57 37 59'.split(' ')
print(solution([int(i) for i in arr_str]))


