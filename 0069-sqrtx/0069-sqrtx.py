import math
class Solution:
    def mySqrt(self, x: int) -> int:
        val=math.sqrt(x)
        return(math.trunc(val))