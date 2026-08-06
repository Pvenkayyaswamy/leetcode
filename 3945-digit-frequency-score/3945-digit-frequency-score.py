class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        sum_ = sum(int(digi) for digi in str(n))
        return sum_