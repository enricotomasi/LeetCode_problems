class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        kind = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0}

        for it in suits:
            kind[it] += 1
        
        for it in kind:
            if kind[it] == 5:
                return "Flush"
        
        cards = { }

        for i in range(14):
            cards[i] = 0
        
        ans = "High Card"

        for it in ranks:
            cards[it] += 1

        for it in cards:
            if cards[it] == 2:
                ans = "Pair"
            elif cards[it] >= 3:
                return "Three of a Kind"

        return ans