import re
ob =  '('
cb = ')'

def isOB(x):
    return x == '('

def isCB(x):
    return x == ')'

def isPair(o , c):
    return isOB(o) and isCB(c)

def strReplace(S, k, repl = ' '):
    return  S[: k] +repl+ S[k+1: ]

def solution(S):
    stk = []

    for k, i in enumerate(S):
        if isOB(i):
            stk.append([i, k])
        elif isCB(i):
            try:
                top, idx = stk.pop()
                if isPair(top , i) is False:
                    S = strReplace(S,idx )
            except IndexError:
               S = strReplace(S, k)
    
    
    while len(stk) > 0:
        _, idx = stk.pop()
        S = strReplace(S, idx)

    return re.sub(' ', '', S)

def solution2(S):
    stk = []
    s = [ i for i in S]

    for i in range(len(s)):
        curr = s[i]
        
        if isOB(curr):
            stk.append([curr, i])
        elif isCB(curr):
            try:
                top, idx = stk.pop()
                if isPair(top , curr) is False:
                    s[idx] = ' '
            except IndexError:
                s[i] = ' '


    while len(stk) > 0:
        _, idx = stk.pop()
        s[idx] = ' '

    return re.sub(' ' , '', ''.join(s))

print(solution2('(abc(d)'))
