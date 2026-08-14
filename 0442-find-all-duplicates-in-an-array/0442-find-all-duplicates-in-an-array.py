class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicates = list(set(x for x in nums if x in seen or seen.add(x)))
        return(duplicates)