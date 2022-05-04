from turtle import right


def isBalanced(root):
    '''
        The algorithm is as follows :

        If node == null -> return 0
        Check left subtree. If not balanced -> return -1
        Check right subtree. If not balanced -> return -1
        The absolute between heights of left and right subtrees. If it is greater than 1 -> return -1.
        If the tree is balanced -> return height( max(left_height, right_height) + 1)
    '''
    if root is None:
        return 0

    leftHeight = isBalanced(root.left)
    if leftHeight == -1: return -1

    rightHeight = isBalanced(root.right)
    if rightHeight == -1: return -1

    if abs(rightHeight - leftHeight) > 1: return -1

    return 1 + max(rightHeight, leftHeight)



