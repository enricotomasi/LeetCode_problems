class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        arr.sort()

        diff = arr[1] - arr[0]

        # print(arr)
        # print(f"diff: {diff}")

        for i in range(1, n - 1):
            # print(f"i: {i}, arr[i + 1]: {arr[i + 1]} arr[i]: {arr[i]} arr[i + 1] - arr[i]: {arr[i + 1] - arr[i]}")
            if (arr[i + 1] - arr[i] != diff):
                return False
        
        return True

        
