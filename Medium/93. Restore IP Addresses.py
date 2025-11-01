def check(addr):
    arr = addr.split('.')
    
    if len(arr) != 4:
        return False
    
    for it in arr:
        if len(it) == 0 or (len(it) > 1 and it[0] == '0'):
            return False
        num = int(it)
        if num < 0 or num > 255:
            return False
    
    return True

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []

        for p0 in range(n):
            for p1 in range(p0 + 1, n):
                for p2 in range(p1 + 1, n):
                    sub0 = s[0  : p0]
                    sub1 = s[p0 : p1]
                    sub2 = s[p1 : p2]
                    sub3 = s[p2 :   ]

                    toadd = sub0 + '.' + sub1 + '.' + sub2 + '.' + sub3

                    if check(toadd):
                        ans.append(toadd)
        
        return ans