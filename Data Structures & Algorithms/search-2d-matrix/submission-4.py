class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = (rows * cols) - 1
        while left <= right:
            mid = (left + right)//2
            row = mid // cols
            col = mid % cols
            current_mid = matrix[row][col]
            if target > current_mid:
                left = mid + 1
            elif target < current_mid:
                right = mid - 1
            elif target == current_mid:
                return True
        return False


