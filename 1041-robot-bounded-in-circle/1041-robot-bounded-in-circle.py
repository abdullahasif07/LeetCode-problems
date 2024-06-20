class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        north_on=False
        south_on=False
        west_on=False
        east_on=False
        x=0
        y=0

        for _ in range(4):
            for i in range(len(instructions)):
                if instructions[i]=="G":
                    if north_on:
                        y+=1
                    elif south_on:
                        y-=1
                    elif east_on:
                        x+=1
                    else:
                        x-=1
                elif instructions[i]=="L":
                    if north_on:
                        north_on=False
                        west_on=True
                    elif south_on:
                        south_on=False
                        east_on=True
                    elif east_on:
                        east_on=False
                        north_on=True 
                    else:
                        west_on=False
                        south_on=True
                else:
                    if north_on:
                        north_on=False
                        east_on=True
                    elif south_on:
                        south_on=False
                        west_on=True
                    elif east_on:
                        east_on=False
                        south_on=True 
                    else:
                        west_on=False
                        north_on=True

            if x==0 and y==0:
                    return True
            else:
                    continue         
        return False                           



        