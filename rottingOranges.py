from collections import deque


def solution(arr):
    N = len(arr)
    M = len(arr[0])

    freshCount = 0
    rotten = []
    directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                freshCount += 1
            elif arr[i][j] == 2:
                rotten.append((i,j))

    
    queue = deque[tuple[int, int]]()

    for i in rotten: queue.append(i)

    minutes = -1
    count =  len(queue)
    curr  = 0


    while len(queue) > 0:
        p, q = queue.popleft()

        curr += 1

        for d in directions:
            x, y = d
            x += p
            y += q

            if -1 < x < N and -1 < y < M and arr[x][y] == 1:
                arr[x][y] = 2
                freshCount -= 1
                queue.append((x, y))
        
        if curr == count:
            count  = len(queue)
            minutes += 1
            curr = 0

    return minutes if freshCount == 0 else -1




grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]

print(solution(grid))