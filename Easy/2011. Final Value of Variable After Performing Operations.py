class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0

        for it in operations:
            if it == "--X" or it == "X--":
                x -= 1
            else:
                x += 1
        
        return x
        