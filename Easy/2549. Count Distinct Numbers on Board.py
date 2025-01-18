class Solution:
    def distinctIntegers(self, n: int) -> int:
        dist = set()
        dist.add(n)

        q = [n]

        while len(q) > 0:
            # print(f"\nq: {q}")
            num = q[0]
            q = q[ 1 : ]

            # print(f"\nnum: {num}")

            for i in range(1, num):
                # print(f" ---> {i}#")
                if num % i == 1:
                    # print(f" ---> i % 1 == 1")
                    if i not in dist:
                        # print(f" ---> bingo")
                        dist.add(i)
                        q += [i]
            # print(f"q: {q}")
            
        # print(f"dist: {dist}")
        return len(dist)

        