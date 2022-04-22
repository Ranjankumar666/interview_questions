class Node:
    def __init__(self, x) -> None:
        self.data = x
        self.child = []


head = None
A, B , C ,  D ,  E = Node(1), Node(2), Node(3), Node(4), Node(5)
head = A
head.child.append(B)
head.child.append(C)
head.child.append(D)

B.child.append(E)

def traverse(node):

    children = node.child

    if len(children) < 0:
        return

    print(node.data, end= " ")
    for i in children:
        traverse(i)

    
    

traverse(head)