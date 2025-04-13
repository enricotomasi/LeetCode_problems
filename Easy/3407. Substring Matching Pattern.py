def search(s, tofind, pos):
    # print(f"\n*****************")
    # print(f"s: {s}, tofind: {tofind}, pos: {pos}")
    
    if tofind == "":
        return pos

    n = len(s)
    
    if tofind != "":
            found = False
            while pos < n:

                for i in range(pos, n):
                    # print(f"{i}# s[i]: {s[i]}")
                    if s[i] == tofind[0]:
                        if len(tofind) == 1:
                            # print("        -> len(tofind) == 1  ok **********")
                            return i + 1
                        # print(f"    -> s[i] == tofind[0]")
                        k = 1
                        for j in range(i + 1, n):
                            # print(f"        -> j: {j} k: {k}")
                            if k >= len(tofind):
                                # print(f"        -> k > len(tofind) ok ******")
                                return j
                            if s[j] != tofind[k]:
                                k = -54
                                # print(f"        -> s[j] != tofind[k] exit")
                                break
                            k += 1
                        
                        # print(f"        -> k: {k} len(tofind): {len(tofind)}")
                        if k >= len(tofind):
                            # print("        -> k >= len(tofind) end cycle, ok ************")
                            return j
                pos += 1
            
            if not found:
                # print("not found return - 1")
                return -1
    
    # print("last check, return -1")
    return -1

class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        first = ""
        second = ""
        f = True

        for c in p:
            if f:
                if c == '*':
                    f = False
                else:
                    first += c
            else:
                second += c
        
        # print(f"first: _{first}_ second: _{second}_")

        pos = search(s, first, 0)
        
        if pos < 0:
            return False

        # print(f"\n *************************** \nFirst ok: pos: {pos}")

        if search(s, second, pos) < 0:
            return False
        
        # print(f"\n *************************** \nsecond ok: pos: {pos}")

        return True
