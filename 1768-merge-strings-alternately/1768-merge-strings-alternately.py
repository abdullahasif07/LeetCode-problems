class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newstr:str=""
        if len(word1) == len(word2):
            for i in range(len(word1)):
                newstr=newstr + word1[i]
                newstr=newstr + word2[i]
        elif len(word1) > len(word2):
            for i in range(len(word2)):
                newstr=newstr + word1[i]
                newstr=newstr + word2[i] 
            rem_len=(len(word1)+len(word2))-len(newstr)
            for i in range(len(word1)-rem_len,len(word1),1):
                newstr=newstr+word1[i]               
        
        elif len(word1) < len(word2):
            for i in range(len(word1)):
                newstr=newstr + word1[i]
                newstr=newstr + word2[i] 
            rem_len=(len(word2)+len(word1))-len(newstr)
            for i in range(len(word2)-rem_len,len(word2),1):
                newstr=newstr+word2[i]
        return newstr        