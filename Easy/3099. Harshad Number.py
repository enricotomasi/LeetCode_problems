class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        copy = x
        sd = 0

        while copy > 0:
            sd += copy % 10
            copy //= 10

        print(sd)
        
        if x % sd == 0:
            return sd
        
        return -1