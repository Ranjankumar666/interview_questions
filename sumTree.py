def isSumTree(node):
    s = 0
    if node is None:
            return 0
    
    elif node.left is None and node.right is None:
        return node.data
    elif node.left and node.right is None:
        s += isSumTree(node.left)
    elif node.right and node.left is None:
        s += isSumTree(node.right)
    else:
        s += isSumTree(node.left) + isSumTree(node.right)
    
    return s


class Node:
    def __init__(self, x) -> None:
        self.data = x
        self.left = None
        self.right = None


head = None
A, B , C ,  D ,  E = Node(10), Node(20), Node(30), Node(10), Node(10)
head = A
head.left = B
head.right = C
head.left.left = D
head.left.right = E


print(isSumTree(head))