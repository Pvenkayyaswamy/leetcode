class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0]*26
        for i in s:
            arr[ord(i)-97]+=1
        for i in t:
            arr[ord(i)-97]-=1
        for l in arr:
            if l !=0:
                return False
        return True