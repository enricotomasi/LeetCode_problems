class Solution:
    def interpret(self, command: str) -> str:
        n = len(command)
        i = 0
        
        ans = ""

        while i < n:
            if command[i] == "G":
                ans += "G"
                i += 1
            else:
                if command[i + 1] == "a":
                    ans += "al"
                    i += 4
                else:
                    ans += "o"
                    i += 2

        return ans
