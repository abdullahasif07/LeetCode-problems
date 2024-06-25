from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates = sorted(coordinates)
        x_1, y_1 = coordinates[0]
        x_2, y_2 = coordinates[1]
    
        if x_1 == x_2:
            for i in range(2, len(coordinates)):
                x, y = coordinates[i]
                if x != x_1:
                    return False
            return True
        else:
            grad = (y_2 - y_1) / (x_2 - x_1)
        
        for i in range(2, len(coordinates)):
            x_prev, y_prev = coordinates[i - 1]
            x, y = coordinates[i]
            
            if x == x_prev:
                return False
            else:
                m = (y - y_prev) / (x - x_prev)
                
            if m != grad:
                return False
                
        return True
