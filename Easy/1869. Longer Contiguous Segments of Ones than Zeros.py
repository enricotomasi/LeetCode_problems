class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        o = 0
        z = 0

        ot = 0
        zt = 0

        last = 2

        for c in s:
            if c == last:
                if c == "1":
                    ot += 1
                    o = max(o, ot)
                else:
                    zt += 1
                    z = max(z, zt)
            else:
                o = max(o, ot)
                z = max(z, zt)

                if c == "1":
                    ot = 1
                    zt = 0
                else:
                    ot = 0
                    zt = 1
            # print(f"o: {o} z: {z}  ***  ot: {ot} zt: {zt}")

            last = c

        o = max(o, ot)
        z = max(z, zt)

        # print(f"   --->  o: {o} z: {z}  ***  ot: {ot} zt: {zt}")
        return o > z
        
        
