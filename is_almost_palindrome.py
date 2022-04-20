from ntpath import join
import re

def replaceAt(s, i):
    return ''.join([ ch for k, ch in enumerate(s) if k != i])

def isPalindrome(s):
    return s == s[::-1]

def isPalindromeIgnore(s, k):
    n = len(s)
    i = 0
    j = n- 1
    
    while i < j :
        if i == k :
          i += 1
          continue
        if j == k:
            j -= 1
            continue
        
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True
###########
def isValidSubPalindrome(s, l, r):

    while( l < r):
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
        
    return True

    
###########
def solution_2(s):
    s = re.sub("[^A-Za-z0-9]+", "", s).lower()
    
    if isPalindrome(s):
        return True
    
    n = len(s)
    i = 0 
    j = n - 1
    

    while i < j:
        if s[i] != s[j]:
            if isValidSubPalindrome(s, i+1, j) or isValidSubPalindrome(s,i , j-1):
                return True
            return False
        
        i += 1
        j -= 1
    
    return True


def solution_v3(s):
    s = re.sub("[^A-Za-z0-9]+", "", s).lower()
    n = len(s)
    i = 0 
    j = n - 1

    if isPalindrome(s):
        return True

    while i < j:
        if s[i] != s[j]:
            if isPalindromeIgnore(s, i) or isPalindromeIgnore(s, j):
                return True
            
            return False
        
        i += 1
        j -= 1
    
    return True

def solution(s):
    s = re.sub("[^A-Za-z0-9]+", "", s).lower()
    n = len(s)
    i = 0 
    j = n - 1

    if isPalindrome(s):
        return True

    while i < j:
        if s[i] != s[j]:
            op = s[:i] + s[i+1:]
            if isPalindrome(op):
                return True
            
            op = s[:j] + s[j+1:]

            if isPalindrome(op):
                return True
            
            return False
        
        i += 1
        j -= 1
    
    return True


print(solution('"cbbcc"'))