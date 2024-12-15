class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = len(word)

        found = False
        first = ""
        second = ""

        for i in range(n):
            if found:
                second += word[i]
            else:
                first += word[i]
                if word[i] == ch:
                    found = True
        
        # print(f" *** {first}---{second} ***")

        if not found and second == "":
            return word
        
        return first[ : : - 1 ] + second
        