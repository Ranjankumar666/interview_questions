from collections import deque


def breathFirstAdjList(graph, start):

    res = []
    q = deque()
    visited = {}

    q.append(start)

    while len(q) > 0:
        t = q.popleft()
        visited[t] = True
        res.append(t)

        for conn in graph[t]:
            if not visited.get(conn, False):
                q.append(conn)


    return res

def depthFirstAdjList(graph, start):

    res = []
    stk = deque()
    stk.append(start)
    visited = {}

    while len(stk) > 0:
        last = stk.pop()

        visited[last] = True
        res.append(last)

        for conn in graph[last]:
            if not visited.get(conn, False):
                stk.append(conn)
    
    return res

def dfsRecursive(graph, start, visited, res):
    if visited.get(start, False):
        return res

    visited[start] = True
    res.append(start)

    for conn in graph[start]:
        dfsRecursive(graph, conn, visited, res)
    
    return res

g = {
    0: [1, 3], 1: [0], 2: [3, 8], 3: [0,2, 4, 5], 4: [3, 6], 5: [3], 6: [4, 7], 7: [6], 8:[2]
}
print(breathFirstAdjList(g, 0))
print(dfsRecursive(g, 0, {}, []))

