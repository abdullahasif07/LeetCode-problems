class Solution:
    def countOdds(self, low: int, high: int) -> int:
        c=high-low+1
       
        if low%2==0:
            return int(c/2)
        else:
            return int(c/2+0.5)
                
        