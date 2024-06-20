import statistics
class Solution:
    def average(self, salary: List[int]) -> float:
        salary=sorted(salary)[1:-1]
        return statistics.mean(salary)
        
        