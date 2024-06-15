class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sortedarr=sorted(arr)
        yes=True
        diff=sortedarr[0]-sortedarr[1]
        for i in range(1,len(sortedarr),1):
            if i+1<len(sortedarr):
                newdiff=sortedarr[i]-sortedarr[i+1]
                if newdiff==diff:
                    yes=True
                else:
                    yes=False
                    return yes    
        return yes

        