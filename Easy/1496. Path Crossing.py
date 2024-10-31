class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s = set()
        s.add((0, 0))
        
        x = 0
        y = 0

        for it in path:
            if it == "N":
                x -= 1
            elif it == "S":
                x += 1
            elif it == "W":
                y -= 1
            else:
                y += 1

            # print(f"{it} {x}, {y}")

            if (x, y) in s:
                return True
            
            s.add((x, y))

        return False




        
