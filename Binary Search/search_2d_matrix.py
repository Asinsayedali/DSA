from typing import List
# FIRST SOLUTION WRITTEN BY ME. complexity O(m * log n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_size = len(matrix[0])-1

        for i in range(len(matrix)):
            if target > matrix[i][row_size]:
                continue
            else:
                low = 0
                high = row_size
                while low <= high:
                    mid = (low+high)//2
                    if matrix[i][mid] < target:
                        low = mid + 1
                    elif matrix[i][mid] > target:
                        high = mid - 1
                    else:
                        return True
        return False
        

# OPTIMIZED SOLUTION WHERE COMPLEXITY IS IN O(LOG(M*N))
# Core idea is we treat the 2d array as a 1d array and map the mid to find the row and column in the 2d array. 
# That is row value is always mid//col in 2d array.. the coloumn no of the value will be always mid%col.
# inshort mid//col gets which row the element is in, mid%col gets which column the element is in. So we get the i and j value to see if value matches the target. 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        left = 0 
        right = (row * col) -1

        while left<=right:
            mid = (left+right)//2
            r = mid // row
            c = mid % col
            value = matrix[r][c]
            if value < target:
                left = mid + 1
            elif value > target:
                right = mid - 1
            else:
                return True
        return False
