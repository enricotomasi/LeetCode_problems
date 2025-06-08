class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        temp = 1
        
        for i in range(n):
            ans += [temp]
            if temp * 10 <= n:
                temp *= 10
            else:
                while temp % 10 == 9 or temp + 1 > n:
                    temp //= 10
                temp += 1
        
        return ans