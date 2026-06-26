class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(c in set(jewels) for c in stones)