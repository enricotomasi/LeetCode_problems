class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        n = len(s)

        # print(f"n: {n}")

        if n != len(goal):
            return False

        for i in range(n):
            
            if s[i] == goal[0]:
                # print(i, s[i])
                pos = (i + 1) % n
                ok = True
                
                for j in range(1, n):
                    # print(f"  ---> pos: {pos} j: {j}   s[pos]: {s[pos]} goal[j]: {goal[j]}")
                    if s[pos] != goal[j]:
                        ok = False
                        # print("  ---> different, exit")
                        break
                    
                    pos += 1
                    pos %= n
                
                if ok:
                    return True

                
        return False


        