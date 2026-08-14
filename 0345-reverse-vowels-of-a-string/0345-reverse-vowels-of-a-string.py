class Solution:
    def reverseVowels(self, s: str) -> str:
        l=list(s)
        left =0
        right = len(s)-1
        char_arr = ['A','E','I','O','U','a','e','i','o','u']
        while (left < right):
            if (l[left] in char_arr and l[right] in char_arr):
                l[left],l[right]=l[right],l[left]
                left+=1
                right-=1
            if(l[right] not in char_arr):
                right-=1
            if(l[left] not in char_arr):
                 left+=1
        return ''.join(l)