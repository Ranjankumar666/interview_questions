from collections import deque

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

# size  = 4
# preReqs = [[2,0],[1,0],[3,1],[3,2],[1,3]]
# size = 6
# preReqs = [
#     (1, 0), (2,1), (2, 5), (0, 3), (4, 3), (3, 5), (4, 5)
# ]
size  = 7
preReqs = [(0, 3), (1, 0), (2, 1), (4, 5), (6, 4), (5, 6)]

print(topSort(size, preReqs))