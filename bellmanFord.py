INF = float('inf')

def solution(edgeList, N, start):
    shortest = { i+1: INF for i in range(N)}
    shortest[start] = 0 


    for _ in range(N-1):
        for  src, dest , wght in edgeList:

            if shortest[src] != INF and shortest[dest] > shortest[src] + wght :
                shortest[dest] = shortest[src] + wght

    return shortest.values()

edgeList = [
    [1, 4, 2],
    [1 , 2, 9],
    [4 , 2, -4],
    [2 , 5, -3],
    [5 , 3, 7], 
    [3 ,2, 3],
    [3 , 1, 5],
    [4, 5, 6]
]
print(solution(edgeList, 5, 1))