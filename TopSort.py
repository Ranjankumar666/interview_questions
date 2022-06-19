from collections import Counter, deque


def topSort(graph, N):
    visited = [False]*N
    inDegree = [0]*N

    res = []

    for v in range(N):
        for adj in graph[v]:
            inDegree[adj] += 1


    stack = deque()

    for i in range(N):
        if inDegree[i] == 0:
            visited[i] = True
            stack.append(i)

    
    while len(stack) > 0:
        top = stack.pop()
        res.append(top)
        visited[top] = True
        
        for n in graph[top]: 
            inDegree[n] -= 1
            if inDegree[n] == 0:
                stack.append(n)
    return res



graph = [
    [3], [], [3], [], [0, 1], [0]
]

print(topSort(graph, len(graph)))