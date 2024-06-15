class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        c=0
        right_sum=0
        left_sum=0
        done_list=[]
        for i in range(len(mat)):
            right_sum+=mat[i][c]
            done_list.append((i,c))
            c+=1
        
        c_2=len(mat[0])-1
        for i in range(len(mat)):
            if (i,c_2) not in done_list:
                left_sum+=mat[i][c_2]
            c_2-=1
                
        return left_sum+right_sum        