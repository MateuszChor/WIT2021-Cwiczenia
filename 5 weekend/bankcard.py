class BankCard:
    def __init__(self,owner,number,provider):
        self.owner = owner
        self.number = number
        self.provider = provider

    def get_number(self,number):
        print(number)

    def get_owner(self,owner):
        print(owner)
        
    def get_provider(self,provider):
        print(provider)    

class BankAccount:
    def __init__(self,owner,balance,bank):
        self.owner = owner
        self.balance = balance
        self.bank = bank

    def get_owner(self,owner):
        print(owner)

    def get_balance(self,balance):
        print(balance)

    def get_bank(self,bank):
        print(bank)

    def set_balance(self,balance):
        print(balance)

class Bank:
    def __init__(self,name,bank_accounts,bank_cards):
        self.name = name 
        self.bank_accounts = bank_accounts
        self.bank_cards = bank_cards
    
    def get_bank_accounts(self,bank_accounts):
        print(bank_accounts)

    def get_bank_cards(self,bank_cards):
        print(bank_cards)

class CreditCard(BankCard):
    def __init__(self, owner, number, provider,balance,payments_history):
        super().__init__(owner, number, provider)
        self.balance = balance
        self.payments_history = payments_history

    def get_balance(self,balance):
        print(balance)

    def set_balance(self,balance):
        print(balance)

    def get_payments_history(self,payments_history):
        print(payments_history)

class GoldenCreditCard(CreditCard):
    def __init__(self, owner, number, provider, balance, payments_history,reward_points):
        super().__init__(owner, number, provider, balance, payments_history)
        self.reward_points = reward_points

    def get_reward_points(self,reward_points):
        print(reward_points)

    def set_reward_points(self,reward_points):
        print(reward_points)

class PremiumBankAccount(BankAccount):
    def __init__(self, owner, balance, bank,financial_manager):
        super().__init__(owner, balance, bank)
        self.financial_manager = financial_manager

    def get_financial_manager(self,financial_manager):
        print(financial_manager)

    def set_financial_manager(self,financial_manager):
        print(financial_manager)

class StudentBankAccount(BankAccount):
    def __init__(self, owner, balance, bank,overdraft_balance,overdraft_limit):
        super().__init__(owner, balance, bank)
        self.overdraft_limit = overdraft_limit
        self.overdraft_balance = overdraft_balance

    def get_overdraft_balance(self,overdraft_balance):
        print(overdraft_balance)
    
    def set_overdraft_balance(self,overdraft_balance):
        print(overdraft_balance)

    def get_overdraft_limit(self,overdraft_limit):
        print(overdraft_limit)

    def set_overdraft_limit(self,overdraft_limit):
        print(overdraft_limit)

