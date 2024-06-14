class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum=0
        s=-999999
        
        if len(accounts)==1:
            return sum(accounts[0])
        
        for i in range(len(accounts)):
           s=0
           s=sum(accounts[i])
           if s>=max_sum:
            max_sum=s
              
        return max_sum       
        