class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        orig = num
        sub = 0
        ans = 0
        
        pa = 0

        for i in range(k):
            sub += (num % 10) * pow(10, pa)
            pa += 1
            num //= 10

        if sub != 0 and orig % sub == 0:
            ans += 1
        
        while num > 0:
            sub += (num % 10) * pow(10, pa)
            sub //= 10   
            num //= 10 

            if sub != 0 and orig % sub == 0:
                print(sub)
                ans += 1

        return ans
