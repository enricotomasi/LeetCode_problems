class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            gifts.sort(reverse = True)
            gifts[0] = floor(sqrt(gifts[0]))
            # print(f"{i}# {gifts}")
        
        ans = 0
        
        for it in gifts:
            ans += it
        
        return ans

        