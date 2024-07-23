class Solution:
    def reverseWords(self, s: str) -> str:
    
        words=[]
        words=s.strip().split()
        words.reverse()
        s=' '.join(words)
        
        return s    