class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if(i%2!=0):
                nums[0]=nums[0]-nums[i]
            else:
                nums[0]=nums[0]+nums[i]
        return nums[0]