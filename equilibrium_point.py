'''
Get the total sum then, aadd curr to left side and get right side bt S - left_side - curr
'''
def sumInRange(arr, start, end):
    s = 0
    for i in range(start, end):
        s += arr[i]

    return s


def solution(arr):
    n = len(arr)
    left_sum = 0
    S = sum(arr)

    for i in range(n):
        if (left_sum == S - left_sum -arr[i]):
            return i + 1

        left_sum += arr[i]
    
    return -1
arr ='1 3 5 2 2'.split(' ')

arr = [ int(i) for i in arr]

print(solution(arr))