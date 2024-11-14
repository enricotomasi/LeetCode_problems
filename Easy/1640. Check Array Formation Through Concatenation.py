class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = dict()

        for it in pieces:         
            if (len(it) > 0):
                d[it[0]] = it[1:]

        # print(d)

        n = len(arr)
        i = 0

        while (i < n):
            # print(f"\n {arr[i]}")
            if (arr[i] in d):
                # print("ok, in dict")
                if i == n -1:
                    return True
                temp = d[arr[i]]
                nt = len(temp)
                # print(f"nt: {nt}")
                i += 1

                if (nt == 0):
                    continue

                for j in range(nt):
                    # print(f"i: {i}  ---  j: {j}")
                    if (i == n):
                        # print("i == n - 1")
                        if (j == nt):
                            # print("j == nt - 1 return True")
                            return True
                        else:
                            # print("j != nt - 1 return False")
                            return False

                    # print(f"  ---> {arr[i]} * {temp[j]}")
                    if (arr[i] != temp[j]):
                        # print("  ---> not in dict, return False")
                        return False
                    i += 1
                    j += 1
            else:
                # print("not in dict, return False")
                return False

        # print("OK, return True")
        return True       
