from typing import List


def to2D(val, width):
    row = val//width 
    col = val%width
    
    return row, col

def to1D(coor , width): 
        return coor[0]*width + coor[1]

    

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0])
        n = len(matrix)
        
        left = (0, 0)
        right  = (n-1, width-1) 
        
    

        while ( to1D(left, width) <= to1D(right, width)) :
            
            mid = to1D(left, width) + (to1D(right, width) - to1D(left, width) )//2
            
            i, j = to2D(mid, width)

            if matrix[i][j] == target:
                return True
            
            if target > matrix[i][j]:
                left = (i, j+1)
            else:
                right = (i , j-1)
        


        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(Solution().searchMatrix(matrix, target)) 