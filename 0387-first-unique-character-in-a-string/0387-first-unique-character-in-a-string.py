class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_coun = {}
        for let in s:
            if let in char_coun:
                char_coun[let] = char_coun.get(let,0)+1
            else:
                char_coun[let] = 1
        for let in s:
            if char_coun.get(let,0) == 1:
                return s.index(let)
        return -1