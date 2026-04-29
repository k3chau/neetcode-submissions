class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        mid = (left + right) // 2
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                array_left = 0
                array_right = len(matrix[mid]) - 1
                while array_left <= array_right:
                    array_mid = (array_left + array_right) // 2
                    if matrix[mid][array_mid] == target:
                        return True
                    elif matrix[mid][array_mid] > target:
                        array_right = array_mid - 1
                    elif matrix[mid][array_mid] < target:
                        array_left = array_mid + 1 
                return False
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid - 1 
            elif matrix[mid][0] < target:
                left = mid + 1
        return False
       

        




        