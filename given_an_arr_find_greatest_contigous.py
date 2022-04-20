def solution(arr: list[int]):
    i= 0
    j = 1
    n = len(arr)

    if (n <= 1):
        return -1

    max_sum = 0
    max_i = i
    max_j = j

    while i < n and j < n:
        curr_sum = arr[i] + arr[j]

        if curr_sum > max_sum:
            max_sum = curr_sum
            max_i = i
            max_j = j

        i += 1
        j += 1

    return (max_i, max_j)

print(solution([1,3, 7, 9, 2, 4]))