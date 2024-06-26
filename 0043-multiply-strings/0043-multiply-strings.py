class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        str_list_1=list(num1)
        str_list_2=list(num2)
        int_list_1=[]
        int_list_2=[]
        
        for char in str_list_1:
            if char=='1':
                int_list_1.append(1)
            elif char=='2':
                int_list_1.append(2)
            elif char=='3':
                int_list_1.append(3)    
            elif char=='4':
                int_list_1.append(4)    
            elif char=='5':
                int_list_1.append(5)
            elif char=='6':
                int_list_1.append(6)
            elif char=='7':
                int_list_1.append(7)
            elif char=='8':
                int_list_1.append(8)
            elif char=='9':
                int_list_1.append(9)   
            else:
                int_list_1.append(0)  

        for char in str_list_2:
            if char=='1':
                int_list_2.append(1)
            elif char=='2':
                int_list_2.append(2)
            elif char=='3':
                int_list_2.append(3)    
            elif char=='4':
                int_list_2.append(4)    
            elif char=='5':
                int_list_2.append(5)
            elif char=='6':
                int_list_2.append(6)
            elif char=='7':
                int_list_2.append(7)
            elif char=='8':
                int_list_2.append(8)
            elif char=='9':
                int_list_2.append(9)   
            else:
                int_list_2.append(0)   

        num1=0
        num2=0

        for num in int_list_1:
            num1=num1*10 + num                                       
        for num in int_list_2:
            num2=num2*10 + num

        return str(num1*num2)
