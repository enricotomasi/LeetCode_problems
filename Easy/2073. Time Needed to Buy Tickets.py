class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0

        while tickets[k] >= 0:
            ans += 1
            new = tickets[0] - 1
            tickets = tickets [ 1 : ]

            if new == 0 and k == 0:
                break
            
            if new > 0:
                tickets += [new]
            
            if len(tickets) == 0:
                break
            
            k -= 1
            if k < 0 :
                k = len(tickets) - 1
            # print(tickets, " **** ", k)
            
        return ans
        