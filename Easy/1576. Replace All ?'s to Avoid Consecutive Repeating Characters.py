class Solution:
    def modifyString(self, s: str) -> str:
        n = len(s)
        
        # print(f"n: {n}")
        
        ans = ""
        last = "a"
        end = "z"
        count = 0

        for i in range(n + 1):
            # print(f"\ni: {i}")

            if i != n:
                c = s[i]
            elif s[n - 1] != "?":
                # print("last char not ?, exit");
                break
            else:
                c = last
            
            # print (f"c: {c}")
            # print (f"count: {count}")
            # print(f"last: {last}")

            if c == "?":
                count += 1
                # print(f" ? Increment count: {count}")
            else:
                if count > 0:
                    # print("Count > 0")
                    start = "@"
                    end = "@"
                    next = "@"
                    
                    if i >= n - 1:
                        end = "z"
                        # print("i == n - 1, end = a")
                    
                    # print (f"setting next i < n - 1: {i} < {n - 1} = {i < n - 1}")
                    if i < n - 1:
                        next = s[i + 1]
                    # print(f"Next: {next}")
                    
                    # print (f"start char find, start: {start}, end = {end}, last: {last}, next: {next}")
                    for j in range(26):
                        if start != '@' and end != "@":
                            break

                        # print(f"  ---> j: {j}")
                        if start == "@":
                            if ord('a') + j != ord(last) and ord('a') + j != ord(next) and ord('a') + j != ord(c):
                                start = chr(ord("a") + j)
                                # print(f"  ---> set start: {start}")
                        elif end == "@":
                            if i < n and ord('a') + j != ord(next) and ord('a') + j != ord(c):
                                end = chr(ord("a") + j)
                                # print(f"  ---> set end: {end}")
                    # print (f"loop end              : {start}, end = {end}, last: {last}, next: {next}")
                             
                    flag = True
                    
                    # print(f"Start cycle, start: {start}, end: {end}, count: {count}")
                    for j in range(count):
                        if flag:
                            ans += start
                        else:
                            ans += end
                        flag = not flag
                    
                # print("Reset counter to zero")
                count = 0

                if i < n:
                    # print(f"adding {c} to ans: {ans}")
                    ans += c
                last = c
            
            # print(f"ans: {ans}")

        return ans

                
        
