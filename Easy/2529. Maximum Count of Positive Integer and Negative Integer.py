class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        n = len(nums)
        # print(f"n: {n}")

        if nums[0] > 0:
            return n
        
        if nums[n - 1] < 0:
            return n

        start = 0
        end = n - 1
        mid = -1

        while (start <= end):
            mid = (start + end) // 2
            # print(f"\nstart: {start} end: {end} mid: {mid}  nums[mid]: {nums[mid]}")

            if nums[mid] == 0:
                # print("zero")
                left = 0
                i = mid - 1
                while i >= 0 and nums[i] == 0:
                    # print(f"left {i}# nums[i]: {nums[i]}")
                    i -= 1
                    left += 1
                
                right = 0
                i = mid + 1
                while i < n and nums[i] == 0:
                    # print(f"right {i}# nums[i]: {nums[i]}")
                    i += 1
                    right += 1

                remove = 1 + left + right
                # print(f"left: {left} right: {right}   *** remove: {remove}")
                
                if remove == n:
                    # print("all zeroes")
                    return 0

                n -= remove
                mid -= left

                # print(f"new n: {n}")
                # print(f"mid: {mid} n - mid: {n - mid}")
                return max(mid, n - mid)
            elif nums[mid] > 0 and nums[mid - 1] < 0:
                # print(f"OK! nums[mid]: {nums[mid]}, nums[mid - 1]: {nums[mid - 1]}")
                return max(mid, n - mid)
            elif nums[mid] <= 0:
                # print("nums[mid] <= 0")
                start = mid + 1
            else:
                # print("nums[mid] > 0")
                end = mid - 1
        
        # print(f"\nmid: {mid}")
        return max(mid, n - mid)
