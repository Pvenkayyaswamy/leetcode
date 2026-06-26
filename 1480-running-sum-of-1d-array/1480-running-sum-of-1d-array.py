class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        sums=[]
        for i in nums:
            sum+=i
            sums.append(sum)
        return sums