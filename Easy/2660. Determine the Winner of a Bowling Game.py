def calc(points):
    bonus = 0
    ans = 0
    
    # print(f"\ncalc: {points}")

    for point in points:
        # print()
        if bonus > 0:
            ans += point * 2
            bonus -= 1
            # print(f"Bonus > 0, add: {point * 2}")
            # print(f"Bonus: {bonus}")
        else:
            # print(f"Bonus <= 0, add: {point}")
            ans += point
        
        if point == 10:
            # print(f"Strike! Bonus = 2!")
            bonus = 2
        
        # print(f"ans: {ans} bonus: {bonus}")
        
    return ans


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        score1 = calc(player1)
        score2 = calc(player2)

        if score1 == score2:
            return 0
        
        if score1 > score2:
            return 1
        
        return 2
        