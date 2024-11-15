class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:       
        n = len(code)
        
        ans = [0 for _ in range(n)]
        
        if k == 0:
            return ans
        
        if k > 0:
            for i in range(n):
                sum = 0
                for j in range(i + 1, i + k + 1):
                    pos = j % n
                    sum += code[pos]
                ans[i] = sum
        else:
            k *= - 1
            for i in range(n):
                # print("i", i)
                sum = 0
                # print("k:", k)
                for j in range(k):
                    # print(f"     ---> j: {j}")
                    pos = i - j - 1
                    if pos < 0:
                        pos = n + pos
                    # print(f"     ---> pos: {pos}")

                    sum += code[pos]
                ans[i] = sum
        
        return ans
