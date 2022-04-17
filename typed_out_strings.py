class Stack:
    def __init__(self) -> None:
        self. v=  []
        self.length = 0

    def push(self,x):
        self.v.append(x)
        self.length += 1
    
    def pop(self):
        try:
            self.length -= 1
            return self.v.pop()
        except IndexError:
            return None

    def peek(self):
        return self.v[self.length -1 ]



def solution(str1, str2):
    stk1 = Stack()
    stk2 = Stack()

    for i in str1:
        if(i == '#'):
            stk1.pop()
        else:
            stk1.push(i)

    for j in str2:
        if(j == '#'):
            stk2.pop()
        else:
            stk2.push(j)
    
    s1 = ''.join(stk1.v)
    s2 = ''.join(stk2.v)

    return s1 == s2

print(solution('a####B', 'b'))

