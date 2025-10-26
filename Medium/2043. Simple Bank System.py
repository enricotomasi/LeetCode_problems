class Bank:
    bank = []
    n = 0

    def __init__(self, balance: List[int]):
        self.bank = []
        
        self.bank.append(-1)
        
        for it in balance:
            self.bank.append(it)
        
        self.n = len(self.bank)

        # print(f"\ninit: n: {self.n} bank: {self.bank}")

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # print(f"\nTransfer: {account1} -> {account2} ${money}")
        # print(f"{self.bank}")
        if account1 < self.n and account2 < self.n and self.bank[account1] - money >= 0:
            self.bank[account1] -= money
            self.bank[account2] += money
            # print(f"{self.bank} --- OK")
            return True
        else:
            # print(f"false")
            return False

    def deposit(self, account: int, money: int) -> bool:
        # print(f"\nDeposit: {account} ${money}")
        # print(f"{self.bank}")
        if account < self.n:
            self.bank[account] += money
            # print(f"{self.bank} --- OK")
            return True
        else:
            # print(f"false")
            return False

    def withdraw(self, account: int, money: int) -> bool:
        # print(f"\nWithdraw: {account} ${money}")
        # print(f"{self.bank}")
        if account < self.n and self.bank[account] - money >= 0:
            self.bank[account] -= money
            # print(f"{self.bank} --- OK")
            return True
        else:
            # print(f"false")
            return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)