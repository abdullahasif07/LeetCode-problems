class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        left_prod=[0] * len(nums) 
        right_prod=[0] * len(nums)
        
        left_prod[0]=1
        right_prod[len(nums)-1]=1
        
        for i in range(1,len(nums),1):
            left_prod[i]=nums[i-1]*left_prod[i-1]

        for i in range(len(nums)-2,-1,-1):
            right_prod[i]=nums[i+1]*right_prod[i+1]
        
        answer=[]
        for i in range(len(nums)):
            answer.append(right_prod[i]*left_prod[i])
            
        return answer    
            