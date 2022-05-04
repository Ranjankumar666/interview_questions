from BST import BinarySearchTree


visited = set()
def goLeft(root, res):
    if root is None:
        return res
     
    if root not in visited:   
        visited.add(root)
        res.append(root.data)
    goLeft(root.left, res)
    
    return res

def goLeaves(root,res):
    
    if root is None:
        return res

    goLeaves(root.left, res)
    if root.left is None and root.right is None:
        if root not in visited:
            res.append(root.data)
            visited.add(root)
    
    
    goLeaves(root.right, res)
    
    
    return res
    
def goRight(root, res):
    if root is None:
        return res
     
    goRight(root.right, res)
    
    if root not in visited:   
        visited.add(root)
        res.append(root.data)
        
   
    
    return res

def printBoundaryView( root):
    # Code here
    res = goLeft(root, [])
    res = goLeaves(root, res)
    res = goRight(root, res)
    
    return res

tree = BinarySearchTree[int]()

for i in [4,2 ,1, 8, 9, 0]:
    tree.add(i)

print(printBoundaryView(tree.root))