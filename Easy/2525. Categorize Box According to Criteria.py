class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume = length * width * height

        bulk = False
        if length >= 10000 or height >= 10000 or width >= 10000 or volume >= 1000000000:
            bulk = True
        
        heavy = False
        
        if mass >= 100:
            heavy = True
        
        if bulk and heavy:
            return "Both"
        
        if not bulk and not heavy:
            return "Neither"
        
        if bulk:
            return "Bulky"
        
        return "Heavy"
        
