class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        for i in range(0,n):
            an=nums[nums[i]]
            ans.append(an)
        return ans