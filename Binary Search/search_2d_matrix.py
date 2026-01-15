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

