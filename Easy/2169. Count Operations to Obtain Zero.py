class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0

        while num1 > 0 and num2 > 0:
            ans += 1
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1
            
            # print(f"{ans}  {num1} {num2}")
        
        return ans
        