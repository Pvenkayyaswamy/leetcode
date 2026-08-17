class Solution:
    def repeatedCharacter(self, s: str) -> str:
        char_coun = {}
        for let in s:
            if let in char_coun:
                char_coun[let] = char_coun.get(let,0)+1
            else:
                char_coun[let] = 1
        
            if char_coun.get(let,0) == 2:
                return let