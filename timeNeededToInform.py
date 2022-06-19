from collections import deque
def dfs(graph, informTime , m):

    if informTime[m] == 0:
        return 0


    brnchs = []
    for sub in graph[m]:
       brnchs.append( informTime[m] + dfs(graph, informTime, sub))

    return max(brnchs)


def timeNeededToInform(managers, headId, informTime):
    N = len(managers)
    hierar = {i: [] for i in range(N)}

    for i, k in enumerate(managers):
        if k != -1:
            val =  hierar.get(k, [])
            val.append(i)
            hierar[k] = val


    return dfs(hierar, informTime, headId)

N ,head, manager,  inform = 10 ,3 ,[8,9,8,-1,7,1,2,0,3,0],  [224,943,160,909,0,0,0,643,867,722]
print(timeNeededToInform(manager, head, inform))