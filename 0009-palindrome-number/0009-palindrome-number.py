class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        rev=0
        while n>0:
            last=n%10
            rev=rev*10+last
            n=n//10
        if x==rev:
            return(bool(1))
        else:
            return(bool(0))
obj=Solution()
val=obj.isPalindrome(121)
print(val)