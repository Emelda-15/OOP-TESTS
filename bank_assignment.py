class BankAccount:
    
    #class variable(interest rate)
    interest_rate = 0.05
    
    #constructor
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        
    #method to deposit an amount
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else: 
             print("The transaction should have some cash")
             
    #method to withraw an amount
    def withdraw(self, amount):
         if 0 < amount <= self.balance:
            self.balance -= amount
         else:
            print("Insufficient funds")
            
    #method to apply interest
    def apply_interest(self):
        self.balance += self.balance * BankAccount.interest_rate
        
    #method to display account information
    def display_account_info(self):
        print(f"account_holder: {self.account_holder}, Balance: {self.balance:.2f}")
        
    #creating objects
account1 = BankAccount("Sarah", 4000)
account2 =BankAccount("Sheba",2000)   

    #display account information 
account1.display_account_info()
account2.display_account_info()

    #perform deposits and wihdraws
account1.deposit(3000)
account1.withdraw(600)
account1.apply_interest()

account2.deposit(3000)
account2.withdraw(600)
account2.apply_interest()




    

 
           
            
        
        
        