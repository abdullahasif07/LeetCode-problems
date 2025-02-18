class Solution(object):
    def findMaxAverage(self, nums, k):
        max_avg = float('-inf')
        sum_num = 0.0
        
        if len(nums) == 1:
            return nums[0]

        for i in range(k):
            sum_num += nums[i]

        max_avg = sum_num / k

        for i in range(k, len(nums)):
            sum_num += nums[i] - nums[i - k]
            avg = sum_num / k
            if avg > max_avg:
                max_avg = avg

        return max_avg