class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n=max(candies)
        boollist=[]
        for i in candies:
            if(i+extraCandies>=n):
                boollist.append(True)
            else:
                boollist.append(False)
        return boollist