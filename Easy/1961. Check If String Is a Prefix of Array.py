class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        n = len(s)
        # print(f"n: {n}, len(words): {len(words)}")
        i = 0

        for word in words:
            # print(f"\n{word}")
            # print(f"i: {i}")
            if i >= n:
                # print(f"i == n - 1, {i} == {n - 1} return True")
                return True

            if len(word) > n - i:
                # print(f"len(word) : {len(word)} > n - 1 : {n - 1}")
                return False
            
            for c in word:
                # print(f"     -> {c}  i : {i}")
                if c != s[i]:
                    # print(f"     -> c ({c}) != s[i]: {s[i]}  <----->  exit")
                    return False
                i += 1
            
        # print("No more words, return true")
        return i >= n
        