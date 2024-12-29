class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        remove = -1
        great = False

        for i in range(n - 1):
            if number[i] == digit:
                remove = i
                if number[i + 1] > number[i]:
                    great = True
                    break
        
        # print(remove)

        if not great and number[n - 1] == digit:
            return number[ : n - 1 ]
               
        if remove < 0:
            return number[ : n - 1]
        
        if remove == 0:
            return number[ 1  : ]

        return number[ 0 : remove] + number[ remove + 1 : n ]
        