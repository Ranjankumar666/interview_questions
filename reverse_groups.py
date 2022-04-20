import math
from linked_list import LinkedList
from m_n_reversals import solution

def getLength(head):
    
    if head is None:
        return 0
    count = 0    
    t= head
    
    while t:
        t = t.next
        count += 1
    
    return count

def reverseGroup(head, k):
    n = getLength(head)
    t = math.floor(n/k)
    i = 1
    j = k
    
    for _ in range(t):
        head = solution(head, i, j)
        i = j + 1
        j += k

        
    return head


ll = LinkedList()

arr = list(map(int,'1 2 3 4 5'.split(' ')))

for i in arr:
    ll.add(i)

ll.head = reverseGroup(ll.head, 3)
ll.print()
        