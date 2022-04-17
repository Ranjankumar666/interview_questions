from lib2to3.pytree import convert


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


def convertToStack(s: Stack, s1: str) -> Stack:
    for i in s1:
        if(i == '#'):
            s.pop()
        else:
            s.push(i)


def solution(str1, str2):
    stk1 = Stack()
    stk2 = Stack()

    convertToStack(stk1, str1)
    convertToStack(stk2, str2)


    s1 = ''.join(stk1.v)
    s2 = ''.join(stk2.v)

    return s1 == s2

print(solution('a####b', 'b'))

