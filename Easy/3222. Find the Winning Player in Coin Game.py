class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        if y < 4:
            return "Bob"

        if y // 4 > x:
            # print("y // 4 > x")
            if x % 2 == 0:
                return "Bob"
            else:
                return "Alice"
        else:
            # print("y // 4 <= x")
            if (y // 4) % 2 == 0:
                return "Bob"
            else:
                return "Alice"
        
