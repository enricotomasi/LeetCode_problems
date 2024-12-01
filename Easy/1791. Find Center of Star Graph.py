class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        i = 1

        while True:
            ok = True
            for it in edges:
                # print(f"\ni: {i} it[0]: {it[0]} it[1]: {it[1]}")
                # print(f"it[0] != i: {it[0] != i}")
                # print(f"it[1] != i: {it[1] != i}")
                # print(f"it[0] != i and it[1] != i: {it[0] != i and it[1] != i}")
                if it[0] != i and it[1] != i:
                    ok = False
                    break
            if ok:
                return i
            
            i += 1
        
        return -1
        