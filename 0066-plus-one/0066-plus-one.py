class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strlist=[str(num) for num in digits]
        newnum=''.join(strlist)
        newnum=int(newnum)
        newnum+=1
        newnum=str(newnum)
        newliststr=[str(num) for num in newnum]
        newlistnum=[int(num) for num in newliststr]
        return newlistnum
        
        