class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        first="f"
        sec="s"
        third="t"
        fourth="u"
        fifth="w"
        sixth="r"
        seventh="x"
        eigth="y"
        ninth="z"
        total=0
        
        for i in range(len(moves)):
            if i % 2==0:
                total+=1
                if moves[i]==[0,0]:
                    first='A'
                elif moves[i]==[0,1]:
                    sec='A'
                elif moves[i]==[0,2]:
                    third='A'
                elif moves[i]==[1,0]:
                    fourth='A'
                elif moves[i]==[1,1]:
                    fifth='A'
                elif moves[i]==[1,2]:
                    sixth='A'
                elif moves[i]==[2,0]:
                    seventh='A'
                elif moves[i]==[2,1]:
                    eigth='A'
                elif moves[i]==[2,2]:
                    ninth='A'
                else:
                    continue    
                if  first==sec==third or fourth==fifth==sixth or seventh==eigth==ninth or first==fourth==seventh or sec==fifth==eigth or third==sixth==ninth or first==fifth==ninth or third==fifth==seventh:
                    return("A") 
                else:
                    continue
        
            else:
                total+=1
                if moves[i]==[0,0]:
                    first='B'
                elif moves[i]==[0,1]:
                    sec='B'
                elif moves[i]==[0,2]:
                    third='B'
                elif moves[i]==[1,0]:
                    fourth='B'
                elif moves[i]==[1,1]:
                    fifth='B'
                elif moves[i]==[1,2]:
                    sixth='B'
                elif moves[i]==[2,0]:
                    seventh='B'
                elif moves[i]==[2,1]:
                    eigth='B'
                elif moves[i]==[2,2]:
                    ninth='B'
                else:
                    continue    
                if  first==sec==third or fourth==fifth==sixth or seventh==eigth==ninth or first==fourth==seventh or sec==fifth==eigth or third==sixth==ninth or first==fifth==ninth or third==fifth==seventh:
                    return("B") 
        if total<9:
            return("Pending")
        else:                
            return("Draw")

