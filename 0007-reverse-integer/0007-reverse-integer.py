class Solution:
    def reverse(self, x: int) -> int:
            n=abs(x)
            rev=0
            while n>0:
                last=n%10
                rev=rev*10+last
                n=n//10
            if x>=0 and rev<=2147483647:
                return rev
            elif x<0 and (0-rev)>-2147483647:
                return(0-rev)
            else:
                return 0
       
obj=Solution()
val=obj.reverse(123)
print(val)