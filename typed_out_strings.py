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


def solution_v2(str1, str2):
    i = len(str1) - 1
    j = len(str2)- 1

    while i >= 0 or j >= 0:
        if str1[i] == '#' or str2[j] == '#':
            if str1[i] == '#' and i >= 0:
                backcount = 2

                while(backcount > 0 ):
                    i -= 1
                    backcount -= 1

                    if ( str1[i] == '#'):
                        backcount += 2

            if str2[j] == '#' and j >= 0:
                backcount = 2

                while(backcount > 0 ):
                    j -= 1
                    backcount -= 1

                    if ( str2[j] == '#') :
                        backcount += 2
                    
        else:
            if ( i < 0 or j < 0):
                return False

            if(str1[i] != str2[j]):
                    return False
            i -= 1
            j -= 1

    return True

def solution(str1, str2):
    stk1 = Stack()
    stk2 = Stack()

    convertToStack(stk1, str1)
    convertToStack(stk2, str2)


    s1 = ''.join(stk1.v)
    s2 = ''.join(stk2.v)

    return s1 == s2

print(solution_v2("aaa###a","aaaa####a"))

