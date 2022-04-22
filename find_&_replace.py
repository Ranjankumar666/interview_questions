
def replace(arr,newArr,  i , x, y):
    x = [ p for p in x]
    y = [ k for k in y]
    n= len(x)
    t = i   
    s = 0

    while s <  n:
        if x[s] != arr[t]:
            return
        
        s += 1
        t += 1

    
    newArr[i: n+i] = y
    

def findAndReplace( S, Q, index, sources, targets):
    # code here 
    S = [ i for i in S]
    newS = [i for i in S]
    
    for i in range(Q):
        currI = index[i]
        sI = sources[i]
        tI = targets[i]
        
        replace(S,newS, currI, sI, tI)
        
    return ''.join(newS)
        
S = 'gforks'
Q = 2
index = [0, 4]
sources = ['g', 'ks']
target = ['geeks', 'geeks']
print(findAndReplace(S, Q, index, sources, target))