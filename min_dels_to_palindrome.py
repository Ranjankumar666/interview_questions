import re

def subCheck(s, left, right):
    while(left < right):
        if(s[left] != s[right]):
            return False
        
        left += 1
        right -= 1

    return True

def check(s):
    return s == s[::-1]

def solution(s):
    s = re.sub('[^A-Za-z0-9]', '', s).lower()
    n = len(s)

    left = 0
    right = n- 1

    count = 0


    while left < right:
        if s[left] != s[right]:
            if subCheck(s, left+1, right) is False:
                count += 1
            if subCheck(s, left, right -1) is False:
                count += 1
        
        left += 1
        right -= 1
    
    return count

print(solution("aebcbda"))
