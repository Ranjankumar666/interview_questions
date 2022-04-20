import re

def solution(s):
    s = re.sub('[^A-Za-z0-9]+', '', s).lower()
    
    n = len(s)
    
    mid = n//2
    i= mid
    j = mid
    
    if n % 2 == 0:
        i = mid - 1
    
    
    while i >= 0 and j < n:
        if s[i] != s[j]:
            return False
            
        i -= 1
        j += 1
    
    return True


print(solution("A man, a plan, a canal: Panama"))