class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        s = set()

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if digits[k] % 2 != 0 or i == j or i == k or j == k or digits[i] == 0 or (digits[i] == 0 and digits[j] == 0) or (digits[i] == 0 and digits[j] == 0 and digits[k] == 0):
                        continue
                    s.add(digits[i] * 100 + digits[j] * 10 + digits[k])
        
        ans = list(s)
        ans.sort()
        return ans
