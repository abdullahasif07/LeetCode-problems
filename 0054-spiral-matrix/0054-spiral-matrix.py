from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
       
        if not matrix or not matrix[0]:
            return []

        final = []

        while matrix:
            final += matrix.pop(0)

            if matrix and matrix[0]:
                for row in matrix:
                    final.append(row.pop())

            if matrix:
                final += matrix.pop()[::-1]

            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    final.append(row.pop(0))

        return final