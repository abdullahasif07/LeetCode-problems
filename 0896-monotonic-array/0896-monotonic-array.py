class Solution:

    def inc(self, nums:List[int])->bool:
        incr=False
        prev_num=nums[0]
        for num in nums:
            if num>=prev_num:
                incr=True
                prev_num=num
            else:
                incr=False
                break
        return incr  

    def dec(self, nums:List[int])->bool:
        decr=False
        prev_num=nums[0]
        for num in nums:
            if num<=prev_num:
                decr=True
                prev_num=num
            else:
                decr=False
                break
        return decr 

    def isMonotonic(self, nums: List[int]) -> bool:
        if self.inc(nums) or self.dec(nums):
            return True
        else:
            return False    


                    