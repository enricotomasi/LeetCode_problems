class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        last = -1
        st = s.split(' ')

        for it in st:
            if it.isnumeric():
                num = int(it)
                if num <= last:
                    return False
                last = num
        
        return True

        