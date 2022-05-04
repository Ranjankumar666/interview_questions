from math import ceil


def getHeight(root):
    if root is None:
        return 0
    
    return 1 + getHeight(root.left)

def isValid(idxToFind, height, node):
    '''
        This function takes an index , the height & the root.
        It then implements Binary Search, until node of interest
    '''
    left = 0
    right = 2**(height - 1) - 1
    count = 1

    while(count < height):
        midOfNode = left + ceil((right - left)/2)

        if idxToFind >= midOfNode:
            node = node.right
            left = midOfNode
        else:
            node = node.left
            right = midOfNode-1
        
        count += 1
    
    return node != None

def countNodes(root):

    if root is None: return 0
    height = getHeight(root);

    if height == 1: return 1

    nodesBeforeLast = 2**(height-1) - 1
    upperBound= nodesBeforeLast
    lowerBound = 0

    left = lowerBound
    right = upperBound

    '''
        Binary search to find all possible right most node
    '''
    while (left < right):
        mid = left + ceil((right - left)/2)

        if isValid(mid, height, root):
            left = mid
        else:
            right = mid-1
    
    return nodesBeforeLast + [2**(height-1) - right + 1]


