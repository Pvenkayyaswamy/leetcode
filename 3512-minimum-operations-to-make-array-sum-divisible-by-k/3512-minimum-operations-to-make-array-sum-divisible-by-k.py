class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s=sum(nums)
        count=0
        while(s>=0):
            if(s%k==0):
                return count
            else:
                s-=1
                count+=1