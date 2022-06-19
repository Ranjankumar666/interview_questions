from queue import PriorityQueue
INF = float('inf')

def solution(times, N , k):
    graph = [[] for i in range(N)]
    k = k -1
        
    for t in times:
        src, dest, wght = t
        graph[src - 1].append((dest -1, wght))
    
    
    q = PriorityQueue()

    shortest = [INF]*N
    shortest[k] = 0

    q.put((k, shortest[k]))

    while not q.empty():
        src, _ = q.get()

        for adj, w in graph[src]:

            if shortest[adj] > shortest[src] + w:
                shortest[adj] = shortest[src] + w
                q.put((adj , shortest[adj]))
        

    
    maxTime = max(shortest)
    return maxTime if maxTime != INF else -1
    
times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
k = 2
print(solution(times,N , k ))

