def rle(n):  
    # print(f"\n************************* {n}")
    ans = ""
    last = n[0]
    count = 1

    for i in range(1, len(n)):
        # print(f"last: {last} count: {count}")
        if n[i] == last:
            count += 1
        else:
            ans += str(count)
            ans += last

            count = 1
            last = n[i]

    ans += str(count)
    ans += last

    # print("********************** ans: {ans}")
    return ans


class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"

        for i in range(n - 1):
            ans = rle(ans)
        
        return ans
        