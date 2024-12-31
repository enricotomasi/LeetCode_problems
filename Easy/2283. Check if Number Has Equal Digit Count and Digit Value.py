class Solution:
    def digitCount(self, num: str) -> bool:
        n = len(num)
        m = [0 for _ in range(10)]

        for digit in num:
            m[ord(digit) - ord('0')] += 1

        # print(m)
        
        for i in range(n):
            # print(f"{i}# num[i]: {num[i]}, m[i]: {m[i]} ")
            if m[i] != ord(num[i]) - ord('0'):
                return False
        
        return True

        
