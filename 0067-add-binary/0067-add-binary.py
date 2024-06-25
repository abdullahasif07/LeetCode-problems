class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a= [int(char) for char in a]
        b= [int(char) for char in b]
        final_list=[]
        c=0
        
        if len(a)<len(b):
            for _ in range(len(b)-len(a)):
                a.insert(0,0)
        elif len(b)<len(a):
            for _ in range(len(a)-len(b)):
                b.insert(0,0)
             

        carry = 0

        for i in range(len(a) - 1, -1, -1):
            total = a[i] + b[i] + carry
            if total == 0:
                final_list.insert(0, 0)
                carry = 0
            elif total == 1:
                final_list.insert(0, 1)
                carry = 0
            elif total == 2:
                final_list.insert(0, 0)
                carry = 1
            elif total == 3:
                final_list.insert(0, 1)
                carry = 1

        if carry == 1:
            final_list.insert(0, 1)

        str_list=[str(i) for i in final_list]
        result = ''.join(str_list)
        return result
    
                 

                            




        