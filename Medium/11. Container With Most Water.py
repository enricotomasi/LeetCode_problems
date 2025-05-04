class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        ans = 0

        start = 0
        end = n - 1

        while start < end:
            area = (end - start) * min(height[start], height[end])
            ans = max(ans, area)
            
            # print(f"start: {start} end: {end}  {height[start]}, {height[end]} area: {area} ans: {ans}")

            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
            
        
        return ans