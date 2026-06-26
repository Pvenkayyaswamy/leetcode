class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for st in operations:
            match st:
                case "X++" | "++X":
                    x+=1
                case "X--" | "--X":
                    x-=1
        return x