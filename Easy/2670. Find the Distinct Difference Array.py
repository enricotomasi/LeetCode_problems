class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        dx = {}

        for it in nums:
            if it in dx:
                dx[it] += 1
            else:
                dx[it] = 1
        
        sx = {}
        
        ans = []

        for it in nums:
            if it in sx:
                sx[it] += 1
            else:
                sx[it] = 1
            
            dx[it] -= 1

            s = 0
            for it2 in sx:
                if sx[it2] >= 1:
                    s += 1
            
            d = 0
            for it2 in dx:
                if dx[it2] >= 1:
                    d += 1
            
            # print(f"\n{it}: s: {s} d: {d}")
            # print(f"sx: {sx}")
            # print(f"dx: {dx}")
            # print(f"result: {s - d}")

            ans += [s - d]
        
        return ans

        
