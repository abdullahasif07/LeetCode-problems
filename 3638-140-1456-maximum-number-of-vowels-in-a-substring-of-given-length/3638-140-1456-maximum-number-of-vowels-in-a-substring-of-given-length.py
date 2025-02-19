class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
      count=0
      count=self.count_vowel(s[:k])

      if len(s)==1:
        return count


      print(f"count: {count}")
      new_count=0
      max_count=0
      max_count=max(max_count,count)

      for i in range(k,len(s)):
        print(f"on char: {s[k]}")
        if s[i] in 'aeiou':
            
            if s[i-k] in 'aeiou':
                print(f"k-ith character: {s[i-k]}")
                new_count=count
                print(f"new count: {new_count}")
                max_count=max(max_count,new_count)
                count=new_count
            else:
                new_count=count+1
                print(f"k-ith character: {s[i-k]}")
                print(f"new count: {new_count}")
                max_count=max(max_count,new_count)
                count=new_count
        else:
          
            if s[i-k] in 'aeiou':
                print(f"k-ith character in 2nd: {s[i-k]}")
                new_count=count-1
                print(f"new count: {new_count}")
                max_count=max(max_count,new_count)
                count=new_count
            else:
                new_count=count
                print(f"k-ith character: {s[i-k]}")
                print(f"new count: {new_count}")
                max_count=max(max_count,new_count)
                count=new_count  
      
      return max_count              




    def count_vowel(self, s):
        count=0
        for i in range(len(s)):
           if s[i] in 'aeiou':
                count+=1
        return count        
