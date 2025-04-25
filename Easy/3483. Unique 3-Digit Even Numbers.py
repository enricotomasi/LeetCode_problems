class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        ans = set()

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or i == k or digits[i] == 0:
                        continue
                    
                    num = (100 * digits[i]) + (10 * digits[j]) + digits[k]
                    # print(num, end = " ")

                    if num % 2 == 0:
                        ans.add(num)
                        # print(" --- OK ---", end = "")

                    # print()

        return len(ans)    