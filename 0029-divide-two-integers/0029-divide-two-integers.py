import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==-2147483648 and divisor==-1:
            return (abs(dividend)-1)
        if -2147483648<=dividend<=2147483647 and -2147483648<=divisor<=2147483647 and divisor!=0:
            return(math.trunc(dividend/divisor))
        