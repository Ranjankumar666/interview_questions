class Stack:
    def __init__(self):
        self.s = []
    
    def pop(self):
        try: 
            return self.s.pop()
        except IndexError:
            return None
    
    def push(self, x):
        self.s.append(x)
    
    def __len__(self):
        return len(self.s)
        
        
class Solution:
    def findMaxLen(ob, S):
        # code here 
        stk = Stack()
        max  = 0
        
        for i in S:
            
            if i == '(':
                stk.push('(')
            if i == ')':
                while len(stk) > 0:
                    res = stk.pop();
                    curr = 0 
                    if res and res == '(': 
                        curr += 1
                    
                    if curr > max:
                        max = curr
        
        return max*2

print(Solution().findMaxLen('()(())('))