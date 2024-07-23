class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        bool_arr=[]
        max_cand=max(candies)

        for i in range(len(candies)):
            if candies[i]+extraCandies >=max_cand:
                bool_arr.append(True)
            else:
                bool_arr.append(False)
        return bool_arr            