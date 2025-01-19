class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money == children:
            return 0
        
        if money < children:
            # print("money < children")
            return -1
        
        if money < 8:
            # print("money < 8")
            return 0
        
        if money == 8 and children > 1:
            return 0

        # print(f"money // 8: {money // 8}")

        for i in range(children, 0, -1):
            spend = i * 8
            rem = i % 8
            remchilds = children - i
            remdollars = money - spend

            # print(f"\n{i}# spend = {spend}  rem = {rem}  remchilds: {remchilds}  remdollars: {remdollars}")
            if spend > money:
                # print("not enough money")
                continue
            
            if spend == money and remchilds == 0:
                # print("ok, all children takes 8")
                return i
            
            if remdollars < remchilds:
                # print("Not enought reminder for other children")
                continue
            
            if remchilds == 1 and remdollars == 4:
                # print(f"remchilds == 1 and remdollars == 4")
                continue
            
            if remchilds == 0 and remdollars != 0:
                # print(f"remchilds == 0 and remdollars != 0")
                continue

            return i           

        if money > children:
            return 0    
        
        return -1