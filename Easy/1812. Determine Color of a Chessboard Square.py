class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        c = (ord(coordinates[0]) - ord('a')) + (ord(coordinates[1]) - ord('0')) 
        
        return c % 2 == 0
